from model.person import Person

class Professor(Person) :
    def __init__(self , name, family, national_id, phone, salary , professor_id , lesson_list):
        self.salary = salary
        self.professor_id = professor_id
        self.lesson_list = lesson_list

        super().__init__(name, family, national_id, phone)

        @property
        def salary(self):
            return self.__salary

        @salary.setter
        def salary(self , salary):
            #validator.salary-validator(salary)
            self.__salary = salary

    def __repr__(self):

        person_info = super().__repr__()


        return f"{person_info} |Professor(salary = {self.salary} , professor_id = {self.professor_id} , lesson_list = {self.lesson_list})"