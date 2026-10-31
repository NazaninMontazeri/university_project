from model.person import Person
from tools.validation import *
from model.professor import *
from model.lesson import *
from model.select_lesson import *


class Student(Person) :
    def __init__(self , name , family , national_id , phone , student_id , field_of_study  , select_lesson = None):

        super().__init__(name , family , national_id , phone)
        self.student_id = student_id
        self.field_of_study = field_of_study
        self.select_lesson = select_lesson

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self , student_id):
        Validator.student_id_validator(student_id)
        self.__student_id = student_id

    @property
    def field_of_study(self):
        return self.__field_of_study

    @property
    def select_lesson(self):
        return self._select_lesson

    @select_lesson.setter
    def select_lesson(self, select_lesson):
        self._select_lesson = select_lesson

    @field_of_study.setter
    def field_of_study(self , field_of_study):
        Validator.field_of_study_validator(field_of_study)
        self.__field_of_study = field_of_study

    def __repr__(self):
        person_info = super().__repr__()
        return f"{person_info} |Student(student_id = {self.student_id} , field_of_study = {self.field_of_study} )"

    def to_tuple(self) :
        return super().to_tuple() + (self.student_id , self.field_of_study)

    def choose_lesson(self , select_lesson_obj):
        Validator.choose_lesson_validator(self.select_lesson)
        self._select_lesson = select_lesson_obj