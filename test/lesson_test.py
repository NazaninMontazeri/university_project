from model.lesson import Lesson

#test passed
#lesson1 = Lesson("math" , 3 , 5674)
#print(lesson1)
#print(lesson1.to_tuple())

#test passed
#lesson1 = Lesson("math" , 3 , 5674)
#lesson1 = Lesson("math1" , 3 , 5674)
#lesson1 = Lesson("" , 3 , 5674)
#lesson1 = Lesson(9786765 , 3 , 5674)
#print(lesson1)

#test Error
#lesson1 = Lesson("python" , 3 , 5674)
#lesson1 = Lesson("python" , "3" , 5674)
lesson1 = Lesson("python" , 0 , 5674)
print(lesson1)