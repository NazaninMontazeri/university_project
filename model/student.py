from model.person import Person

class Student(Person) :
    def __init__(self , name , family , national_id , phone , student_id , fied_of_study ):

        super().__init__(name , family , national_id , phone)
        self.student_id = student_id
        self.fied_of_study = fied_of_study

    def __repr__(self):
        person_info = super().__repr__()
        return f"{person_info} |Student(student_id = {self.student_id} , fied_of_study = {self.fied_of_study} )"
