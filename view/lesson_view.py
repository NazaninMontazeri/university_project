from tkinter import *
from tkinter import ttk, messagebox
from controller.lesson_controller import LessonController


class LessonView:
    def __init__(self):
        self.controller = LessonController()

        self.win = Toplevel()
        self.win.geometry("650x350")
        self.win.title("Lessons")

        # Name
        Label(self.win, text="Name Lesson").place(x=20, y=20)
        self.name_lesson = StringVar()
        Entry(self.win, textvariable=self.name_lesson).place(x=120, y=20)

        # Units
        Label(self.win, text="Units").place(x=20, y=60)
        self.units = IntVar()
        Entry(self.win, textvariable=self.units).place(x=120, y=60)

        # Lesson Code
        Label(self.win, text="Lesson Code").place(x=20, y=100)
        self.lesson_code = IntVar()
        Entry(self.win, textvariable=self.lesson_code).place(x=120, y=100)

        # Table
        self.table = ttk.Treeview(self.win, show="headings", columns=[1, 2, 3])
        self.table.place(x=280, y=20, width=330, height=280)

        self.table.column(1, width=100)
        self.table.column(2, width=80)
        self.table.column(3, width=100)

        self.table.heading(1, text="Name")
        self.table.heading(2, text="Units")
        self.table.heading(3, text="Code")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(self.win, text="Save", command=self.save_click).place(x=50, y=160)
        self.reset_form()

    def reset_form(self):
        self.name_lesson.set("")
        self.units.set(0)
        self.lesson_code.set(0)

        for item in self.table.get_children():
            self.table.delete(item)

        success, lessons = self.controller.find_all_lesson()
        if success:
            for lesson in lessons:
                self.table.insert("", END, values=lesson.to_tuple())

    def save_click(self):
        success, message = self.controller.save_lesson(
            self.name_lesson.get(),
            self.units.get(),
            self.lesson_code.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    def table_click(self, event):
        selected_row = self.table.focus()
        selected_lesson = self.table.item(selected_row)["values"]

        if selected_lesson:
            self.name_lesson.set(selected_lesson[0])
            self.units.set(int(selected_lesson[1]))
            self.lesson_code.set(int(selected_lesson[2]))