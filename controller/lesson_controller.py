from model.lesson import Lesson
from data_access.data.lesson_da import LessonDa

class LessonController:
    def __init__(self):
        self.lesson_da = LessonDa()

    def save(self, name_lesson, units, lesson_code):
        try:
            new_lesson = Lesson(name_lesson, units, lesson_code)
            self.lesson_da.save(new_lesson)
            return True, "Lesson saved successfully."
        except Exception as e:
            return False, f"Error: {e}"

    def find_all(self):
        try:
            lessons = self.lesson_da.find_all()
            return True, lessons
        except Exception as e:
            return False, f"Error: {e}"