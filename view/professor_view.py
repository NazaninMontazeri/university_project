from tkinter import *
from tkinter import ttk, messagebox
from controller.professor_controller import ProfessorController


class ProfessorView:
    def __init__(self):
        self.controller = ProfessorController()

        self.win = Toplevel()
        self.win.geometry("850x380")
        self.win.title("Professors")

        # Name
        Label(self.win, text="Name").place(x=20, y=20)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).place(x=120, y=20)

        # Family
        Label(self.win, text="Family").place(x=20, y=60)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family).place(x=120, y=60)

        # National ID
        Label(self.win, text="National Id").place(x=20, y=100)
        self.national_id = StringVar()
        Entry(self.win, textvariable=self.national_id).place(x=120, y=100)

        # Phone
        Label(self.win, text="Phone").place(x=20, y=140)
        self.phone = StringVar()
        Entry(self.win, textvariable=self.phone).place(x=120, y=140)

        # Salary
        Label(self.win, text="Salary").place(x=20, y=180)
        self.salary = DoubleVar()
        Entry(self.win, textvariable=self.salary).place(x=120, y=180)

        # Professor ID
        Label(self.win, text="Professor Id").place(x=20, y=220)
        self.professor_id = IntVar()
        Entry(self.win, textvariable=self.professor_id).place(x=120, y=220)

        # Lesson
        Label(self.win, text="Lesson Name").place(x=20, y=260)
        self.professor_lesson = StringVar()
        Entry(self.win, textvariable=self.professor_lesson).place(x=120, y=260)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5, 6, 7])
        self.table.place(x=280, y=20, width=540, height=280)

        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=90)
        self.table.column(4, width=90)
        self.table.column(5, width=70)
        self.table.column(6, width=70)
        self.table.column(7, width=80)

        self.table.heading(1, text="Name")
        self.table.heading(2, text="Family")
        self.table.heading(3, text="National Id")
        self.table.heading(4, text="Phone")
        self.table.heading(5, text="Salary")
        self.table.heading(6, text="Prof Id")
        self.table.heading(7, text="Lesson")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click).place(x=50, y=310)
        self.reset_form()

    def reset_form(self):
        self.name.set("")
        self.family.set("")
        self.national_id.set("")
        self.phone.set("")
        self.salary.set(0.0)
        self.professor_id.set(0)
        self.professor_lesson.set("")

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Professors On Table
        success, professors = self.controller.find_all_professors()
        if success:
            for professor in professors:
                self.table.insert("", END, values=professor.to_tuple())

    def save_click(self):
        success, message = self.controller.save_professor(
            self.name.get(),
            self.family.get(),
            self.national_id.get(),
            self.phone.get(),
            self.salary.get(),
            self.professor_id.get(),
            self.professor_lesson.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected_row = self.table.focus()
        selected_professor = self.table.item(selected_row)["values"]

        if selected_professor:
            self.name.set(selected_professor[0])
            self.family.set(selected_professor[1])
            self.national_id.set(selected_professor[2])
            self.phone.set(selected_professor[3])
            self.salary.set(float(selected_professor[4]))
            self.professor_id.set(int(selected_professor[5]))
            self.professor_lesson.set(selected_professor[6])