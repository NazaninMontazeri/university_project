import os
import pickle

class StudentDa:
    def __init__(self):
        self.filename = "data_access/data/student.dat"
        self.student_list = self.find_all()

    def save(self , student):
        self.student_list.append(student)
        file = open(self.filename , "wb")
        pickle.dump(self.student_list , file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            student_list = pickle.load(file)
            file.close()
            return student_list