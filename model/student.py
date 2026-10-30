from model.person import Person

class Student(Person) :
    def __init__(self , name , family , national_id , phone , student_id , fied_of_study  , selected_lesson = None):

        super().__init__(name , family , national_id , phone)
        self.student_id = student_id
        self.fied_of_study = fied_of_study
        self.selected_lesson = selected_lesson

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self , student_id):
        #Validator.student_id_validator(student_id)
        self.__student_id = student_id

    @property
    def fied_of_study(self):
        return self.__fied_of_study

    @fied_of_study.setter
    def fied_of_study(self , fied_of_study):
        #Validator.fied_of_study_validator(fied_of_study)
        self.__fied_of_study = fied_of_study

    def __repr__(self):
        person_info = super().__repr__()
        return f"{person_info} |Student(student_id = {self.student_id} , fied_of_study = {self.fied_of_study} )"

    def to_tuple(self) :
        return super().to_tuple() + (self.student_id , self.fied_of_study)

