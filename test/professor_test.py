from model.professor import Professor
from tools.validation import *
from data_access.data.professor_da import ProfessorDa
from business_logic.professor_bl import ProfessorBL
from controller.professor_controller import ProfessorController

#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 4032998987, "math")
#print(pro1)
#print(pro1.to_tuple())

#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", "20", 4032998987, "sci")
#print(pro1)
#pro2 = Professor("sara", "Ahmadi", "0019999924", "09127778888", -100, "40124", "physics")
#pro2 = Professor("sara", "Ahmadi", "0019999924", "09127778888", 100, 4032998987 , "physics")
#print(pro2)


#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, "40329u", "math")
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, -40329,  "sci")
#print(pro1)
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, "math")
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 0, "math")
#print(pro1)

#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, "math")
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, )
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, 12344)
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, "sci9")
#print(pro1)

#test passed
#pro2 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, "math")
#print(pro2)
#pro_da = ProfessorDa()
#print(pro_da.find_all())
#pro_da.save(pro2)
#print(pro_da.find_all())


#test passed
#pro1 = Professor("fati", "fatiil", "0098765432", "09123456789", 40 ,403296328, "python")
#pro2 = Professor("reza", "rezaii", "0091265432", "09125556789", 80 ,44444444, "math")
#print(pro1)
#print(pro2)
#bl = ProfessorBL()
#bl.save_professor(pro1)
#print("Done")
#bl.save_professor(pro2)

#test Error
controller = ProfessorController("reza", "rezaii", "0091265432", "09125556789", 80  , 44444444, "math")
print(controller)