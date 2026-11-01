from model.student import *
from data_access.data.student_da import StudentDa
from business_logic.student_bl import StudentBL
from controller.student_controller import StudentController

#test passed
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , 403298329 , "engineer" )
#print(stu)
#print(stu.to_tuple())

#test passed
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , "403298329" , "engineer" )
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , "k" , "engineer" )
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , -999 , "engineer" )
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , 0 , "engineer" )
#print(stu)

#test passed
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , 99998765 , "engineer" )
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , 99998765 , "engineer4" )
#stu = Student("farnaz" , "farahmandi" , "0087965645" , "09876543567" , 99998765 , 678889 )
#print(stu)

#test passed
#student = Student("ali", "alipour", "0025467898", "09123456789" ,403298329, "computer")
#professor = Professor("fati", "fatiil", "0098765432", "09123456789", 40, 98767655, "python")

#lesson1 = Lesson("python", 4, 5677)
#lesson2 = Lesson("math", 3, 1234)
#reg1 = SelectLesson(student, professor, lesson1)
#reg2 = SelectLesson(student, professor, lesson2)
#student.choose_lesson(reg1)
#student.choose_lesson(reg2)

#test passed
#studenttt = Student("fati", "fatiil", "0098765432", "09123456789", 40, "engineer", "python")
#print(studenttt)
#stu_da = StudentDa()
#print(stu_da.find_all())
#stu_da.save(studenttt)
#print(stu_da.find_all())

#test passed
#stud1 = Student("fati", "fatiil", "0098765432", "09123456789", 403296328, "engineer", "python")
#stud2 = Student("reza", "rezaii", "0091265432", "09125556789", 403296328, "computer", "math")
#print(stud1)
#print(stud2)
#bl = StudentBL()
#bl.save_student(stud1)
#print("Done")
#bl.save_student(stud2)

#test passed
#controller = StudentController()
#success , message = controller.save_student("reza", "rezaii", "0091265432", "09125556789", 403296328, "computer")
#print(success)
#print(message)