import os
import pickle

class ProfessorDa:
    def __init__(self):
        self.filename = "data_access/data/professor_dat"
        self.professor_list =self.find_all()

    def save(self , professor):
        self.professor_list.append(professor)
        file = open(self.filename , "wb")
        pickle.dump(self.professor_list , file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename , "rb")
            professor_list = pickle.load(file)
            file.close()
            return professor_list