from model.professor import Professor
from tools.validation import *

#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, "40329", ["math", "sci"])
#print(pro1)
#pro1.add_lesson("math")
#pro1.add_lesson("python")
#print(pro1.to_tuple())

#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", "20", "40329", ["math", "sci"])
#print(pro1)
#pro2 = Professor("sara", "Ahmadi", "0019999924", "09127778888", -100, "40124", ["physics"])
#print(pro2)


#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, "40329u", ["math", "sci"])
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, -40329, ["math", "sci"])
#print(pro1)
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, ["math", "sci"])
#print(pro1)

#test passed
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, ["math", "sci"])
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, [])
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, [12344, "sci"])
#pro1 = Professor("ali", "Ahmadi", "0012345678", "09120000000", 20, 40329, ["sci"])
#print(pro1)