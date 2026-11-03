from model.select_lesson import *
from model.student import Student
from model.professor import Professor
from model.lesson import Lesson
from data_access.data.select_lesson_da import SelectLessonDa
from controller.select_lesson_controller import SelectLessonController
from data_access.data.student_da import StudentDa
from data_access.data.professor_da import ProfessorDa
from data_access.data.lesson_da import LessonDa

#test passed
#lesson = Lesson("python" , 4 , 5677)
#student = Student("ali" , "alipour" , "0025467898" , "09876542345" , 403298329 , "computer")
#professor = Professor("fati" , "fatiil" , "0098765432" , "09123456789" , 40 ,98767655 , "python")

#select_lesson1 = SelectLesson(student , professor , lesson)
#print(select_lesson1)

#test passed
#lesson = Lesson("python" , 4 , 5677)
#student = Student("ali" , "alipour" , "0025467898" , "09876542345" , 403298329 , "computer")
#professor = Professor("fati" , "fatiil" , "0098765432" , "09123456789" , 40 ,98767655 , "python")
#score = Score("2024-6-6" , 20)

#select_lesson1 = SelectLesson(student , professor , lesson )
#select_lesson1.assign_score(score)
#print(select_lesson1)
#print(select_lesson1.to_tuple())

#test passed
#lesson = Lesson("python" , 4 , 5677)
#student = Student("ali" , "alipour" , "0025467898" , "09876542345" , 403298329 , "computer")
#professor = Professor("fati" , "fatiil" , "0098765432" , "09123456789" , 40 ,98767655 , "python")
#score1 = Score("2024-6-6" , 20)

#select_lesson1 = SelectLesson(student , professor , lesson )
#select_lesson1.assign_score(score1)
#print(select_lesson1)
#score2 = Score("2024-6-7", 15)
#select_lesson1.assign_score(score2)

#test passed
#lesson = Lesson("python", 4, 5677)
#student = Student("ali", "alipour", "0025467898", "09876542345", 403298329, "computer")
#professor = Professor("fati", "fatiil", "0098765432", "09123456789", 40, 98767655, "python")

#select_lesson1 = SelectLesson(student, professor, lesson)
#student.choose_lesson(select_lesson1)
#print("before score:", select_lesson1)
#da = SelectLessonDa()
#da.save(select_lesson1)
#print(da.find_all())

#score = Score("2024-06-06", 20)
#select_lesson1.assign_score(score)
#print("after score:", select_lesson1)
#da.update(select_lesson1)
#print(da.find_all())


#test ٍpassed
#lesson = Lesson("python", 4, 5677)
#student = Student("ali", "alipour", "0025467898", "09876542345", 403298329, "computer")
#professor = Professor("fati", "fatiil", "0098765432", "09123456789", 40, 98767655, "python")

#select_lesson1 = SelectLesson(student, professor, lesson)
#student.choose_lesson(select_lesson1)

#StudentDa().save(student)
# ProfessorDa().save(professor)
# LessonDa().save(lesson)
# SelectLessonDa().save(select_lesson1)

# controller = SelectLessonController()

# print("--- Test 1: First Score ---")
# success1, msg1 = controller.submit_score(403298329, 20, "2024-06-06")
# print(f"Success: {success1}, Message: {msg1}")


# print("\n--- Test 2: Duplicate Score ---")
# success2, msg2 = controller.submit_score(403298329, 15, "2024-06-07")
# print(f"Success: {success2}, Message: {msg2}")


# print("\n--- Test 3: Register Lesson (via Controller) ---")
# new_student = Student("sara", "ahmadi", "0011223344", "09121112233", 403298330, "math")
# StudentDa().save(new_student)

# controller = SelectLessonController() # ساختن مجدد کنترلر تا دانشجوی جدید رو بشناسه
# success3, msg3 = controller.register_lesson(student_id=403298330, professor_id=98767655, lesson_code=5677)
#print(f"Success: {success3}, Message: {msg3}")