from tkinter import *
from tkinter import ttk, messagebox
from controller.student_controller import StudentController


class StudentView:
    def __init__(self):
        self.controller = StudentController()

        self.win = Toplevel()
        self.win.geometry("750x350")
        self.win.title("Students")

        # Student ID
        Label(self.win, text="Student Id").place(x=20, y=20)
        self.student_id = IntVar()
        Entry(self.win, textvariable=self.student_id).place(x=100, y=20)

        # Name
        Label(self.win, text="Name").place(x=20, y=60)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).place(x=100, y=60)

        # Family
        Label(self.win, text="Family").place(x=20, y=100)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family).place(x=100, y=100)

        # National ID
        Label(self.win, text="National Id").place(x=20, y=140)
        self.national_id = StringVar()
        Entry(self.win, textvariable=self.national_id).place(x=100, y=140)

        # Phone
        Label(self.win, text="Phone").place(x=20, y=180)
        self.phone = StringVar()
        Entry(self.win, textvariable=self.phone).place(x=100, y=180)

        # Field
        Label(self.win, text="Field").place(x=20, y=220)
        self.field_of_study = StringVar()
        Entry(self.win, textvariable=self.field_of_study).place(x=100, y=220)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5, 6])
        self.table.place(x=250, y=20, width=480, height=250)

        self.table.column(1, width=80)
        self.table.column(2, width=80)
        self.table.column(3, width=90)
        self.table.column(4, width=90)
        self.table.column(5, width=70)
        self.table.column(6, width=70)


        self.table.heading(1, text="Name")
        self.table.heading(2, text="Family")
        self.table.heading(3, text="National Id")
        self.table.heading(4, text="Phone")
        self.table.heading(5, text="Student Id")
        self.table.heading(6, text="Field")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click).place(x=50, y=280)
        self.reset_form()


    def reset_form(self):
        self.student_id.set(0)
        self.name.set("")
        self.family.set("")
        self.national_id.set("")
        self.phone.set("")
        self.field_of_study.set("")

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Students On Table
        success, students = self.controller.find_all_student()
        if success:
            for student in students:
                self.table.insert("", END, values=student.to_tuple())

    def save_click(self):
        success, message = self.controller.save_student(
            self.name.get(),
            self.family.get(),
            self.national_id.get(),
            self.phone.get(),
            self.student_id.get(),
            self.field_of_study.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)


    def table_click(self, event):
        selected_row = self.table.focus()
        selected_student = self.table.item(selected_row)["values"]

        if selected_student:
            self.name.set(selected_student[0])
            self.family.set(selected_student[1])
            self.national_id.set(selected_student[2])
            self.phone.set(selected_student[3])
            self.student_id.set(int(selected_student[4]))
            self.field_of_study.set(selected_student[5])