

class Lesson :
    def __init__(self , name_lesson , units , lesson_code):
        self.name_lesson = name_lesson
        self.units = units
        self.lesson_code = lesson_code

    def __repr__(self):
        return f"Lesson(name_lesson = {self.name_lesson} , units = {self.units} , lesson_code = {self.lesson_code})"

    def to_tuple(self):
        return self.name_lesson , self.units , self.lesson_code