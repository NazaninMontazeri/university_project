from model.person import Person
from tools.validation import Validator

class Professor(Person) :
    def __init__(self , name, family, national_id, phone, salary , professor_id , lesson_list):

        super().__init__(name, family, national_id, phone)
        self.salary = salary
        self.professor_id = professor_id
        self.lesson_list = lesson_list

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
        #validator.professor_id_validator(professor_id)
        self.__professor_id = professor_id

    @property
    def lesson_list(self):
        return self.__lesson_list

    @lesson_list.setter
    def lesson_list(self, lesson_list):
        # validator.lesson_list_validator(lesson_list)
        self.__lesson_list = lesson_list

    def __repr__(self):

        person_info = super().__repr__()

        return f"{person_info} |Professor(salary = {self.salary} , professor_id = {self.professor_id} , lesson_list = {self.lesson_list})"

    def to_tuple(self):
        return super().to_tuple() + (self.salary , self.professor_id , self.lesson_list)

    def add_lesson(self , new_lesson):
        if new_lesson not in self.lesson_list :
            self.lesson_list.append(new_lesson)
            print(f"Lesson {new_lesson} added successfully")
        else:
            print(f"Lesson {new_lesson} already exists")