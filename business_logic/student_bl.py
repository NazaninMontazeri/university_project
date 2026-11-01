from  data_access.data.student_da import StudentDa

class StudentBL:
    def __init__(self):
        self.student_da = StudentDa()

    def save_student(self , student):
        all_students = self.student_da.find_all()
        for existing_student in all_students:
            if existing_student.student_id == student.student_id:
                raise ValueError(f"Student ID {student.student_id} already exists!")
        self.student_da.save(student)
        return "Student saved successfully."