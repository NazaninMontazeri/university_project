import os
import pickle

class SelectLessonDa:
    def __init__(self):
        self.filename = "data_access/data/select_lesson.dat"
        self.select_lesson_list = self.find_all()

    def save(self , select_lesson):
        self.select_lesson_list.append(select_lesson)
        file = open(self.filename , "wb")
        pickle.dump(self.select_lesson_list , file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            select_lesson_list = pickle.load(file)
            file.close()
            return select_lesson_list