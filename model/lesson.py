from tools.validation import *

class Lesson :
    def __init__(self , name_lesson , units , lesson_code):
        self.name_lesson = name_lesson
        self.units = units
        self.lesson_code = lesson_code

    @property
    def name_lesson(self):
        return self.__name_lesson

    @name_lesson.setter
    def name_lesson(self , name_lesson):
        Validator.name_lesson_validator(name_lesson)
        self.__name_lesson = name_lesson

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self , units):
        Validator.units_validator(units)
        self.__units = units

    @property
    def lesson_code(self):
        return self.__lesson_code

    @lesson_code.setter
    def lesson_code(self , lesson_code):
        Validator.lesson_code_validator(lesson_code)
        self.__lesson_code = lesson_code

    def __repr__(self):
        return f"Lesson(name_lesson = {self.name_lesson} , units = {self.units} , lesson_code = {self.lesson_code})"

    def to_tuple(self):
        return self.name_lesson , self.units , self.lesson_code