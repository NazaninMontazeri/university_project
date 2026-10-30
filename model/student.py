from model.person import Person
from tools.validation import *

class Student(Person) :
    def __init__(self , name , family , national_id , phone , student_id , field_of_study  , selected_lesson = None):

        super().__init__(name , family , national_id , phone)
        self.student_id = student_id
        self.field_of_study = field_of_study
        self.selected_lesson = selected_lesson

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

    @field_of_study.setter
    def field_of_study(self , field_of_study):
        Validator.field_of_study_validator(field_of_study)
        self.__field_of_study = field_of_study

    def __repr__(self):
        person_info = super().__repr__()
        return f"{person_info} |Student(student_id = {self.student_id} , fied_of_study = {self.field_of_study} )"

    def to_tuple(self) :
        return super().to_tuple() + (self.student_id , self.field_of_study)

    #def choose_lesson(self):
    #اول بقیه کلاس هارو بساز بعد بیا اینو کامل کن