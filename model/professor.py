from model.person import Person
from tools.validation import Validator

class Professor(Person) :
    def __init__(self , name, family, national_id, phone, salary , professor_id , professor_lesson):

        super().__init__(name, family, national_id, phone)
        self.salary = salary
        self.professor_id = professor_id
        self.professor_lesson = professor_lesson

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self , salary):
        Validator.salary_validator(salary)
        self.__salary = salary

    @property
    def professor_id(self):
        return self.__professor_id

    @professor_id.setter
    def professor_id(self, professor_id):
        Validator.professor_id_validator(professor_id)
        self.__professor_id = professor_id

    @property
    def professor_lesson(self):
        return self.__professor_lesson

    @professor_lesson.setter
    def professor_lesson(self, professor_lesson):
        Validator.professor_lesson_validator(professor_lesson)
        self.__professor_lesson = professor_lesson

    def __repr__(self):

        person_info = super().__repr__()

        return f"{person_info} |Professor(salary = {self.salary} , professor_id = {self.professor_id} , professor_lesson = {self.professor_lesson})"

    def to_tuple(self):
        return super().to_tuple() + (self.salary , self.professor_id , self.professor_lesson)