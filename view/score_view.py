from tkinter import *
from tkinter import ttk, messagebox
from controller.select_lesson_controller import SelectLessonController


class ScoreView:
    def __init__(self):
        self.controller = SelectLessonController()

        self.win = Toplevel()
        self.win.geometry("750x350")
        self.win.title("Submit Score")

        # Student ID
        Label(self.win, text="Student Id").place(x=20, y=20)
        self.student_id = IntVar()
        Entry(self.win, textvariable=self.student_id).place(x=120, y=20)

        # Score Value
        Label(self.win, text="Score").place(x=20, y=60)
        self.score_value = DoubleVar()
        Entry(self.win, textvariable=self.score_value).place(x=120, y=60)

        # Score Date
        Label(self.win, text="Date ").place(x=20, y=100)
        self.score_date = StringVar()
        Entry(self.win, textvariable=self.score_date).place(x=120, y=100)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3, 4, 5])
        self.table.place(x=280, y=20, width=450, height=250)

        self.table.column(1, width=70)
        self.table.column(2, width=90)
        self.table.column(3, width=90)
        self.table.column(4, width=90)
        self.table.column(5, width=70)

        self.table.heading(1, text="Student Id")
        self.table.heading(2, text="Student Name")
        self.table.heading(3, text="Professor")
        self.table.heading(4, text="Lesson")
        self.table.heading(5, text="Score")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Submit", command=self.submit_click).place(x=50, y=150)

        self.reset_form()

    def reset_form(self):
        self.student_id.set(0)
        self.score_value.set(0.0)
        self.score_date.set("")

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Select Lessons On Table
        success, registers = self.controller.find_all_select_lesson()
        if success:
            for reg in registers:
                student_id = reg.student.student_id
                student_name = reg.student.name
                professor_name = reg.professor.name
                lesson_name = reg.lesson.name_lesson
                score_value = reg.score.score_value if reg.score else "None"

                values = (student_id, student_name, professor_name, lesson_name, score_value)
                self.table.insert("", END, values=values)

    def submit_click(self):
        success, message = self.controller.submit_score(
            self.student_id.get(),
            self.score_value.get(),
            self.score_date.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected_row = self.table.focus()
        selected_reg = self.table.item(selected_row)["values"]

        if selected_reg:
            self.student_id.set(int(selected_reg[0]))