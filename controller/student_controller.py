from  business_logic.student_bl import StudentBL
from model.student import Student

class StudentController:
    def __init__(self):
        self.student_bl = StudentBL()

    def save_student(self , name , family , national_id , phone , student_id , field_of_study):

        try:
            student = Student(name , family , national_id , phone , student_id , field_of_study)
            self.student_bl.save_student(student)
            return True , "Student saved successfully"

        except Exception as e :
            return False , f"Save Failed : {e}"

    def find_all_student(self):
        try:
            students = self.student_bl.student_da.find_all()
            return True , students
        except Exception as e:
            return False , f"Error Fetching students: {e}"