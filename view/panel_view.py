from tkinter import *

from view import *

class PanelView:
    def student_click(self):
        student_ui = StudentView()

    def professor_click(self):
        professors_ui = ProfessorView()

    def lesson_click(self):
        lesson_ui = LessonView()

    def score_click(self):
        score_ui = ScoreView()

    def select_lesson_click(self):
        select_lesson_ui = SelectLessonView()

    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x400")

        Button(self.win , text = "Student" , width = 20 , command = self.student_click).place(x = 30 , y = 30)
        Button(self.win , text = "Professor" , width = 20 , command = self.professor_click).place(x = 30 , y = 80)
        Button(self.win , text = "Lesson" , width = 20 , command = self.lesson_click).place(x = 30 , y = 130)
        Button(self.win , text = "Score" , width = 20 , command = self.score_click).place(x = 30 , y = 180)
        Button(self.win , text = "Select Lesson" , width = 20 , command = self.select_lesson_click).place(x = 30 , y = 230)

        self.win.mainloop()