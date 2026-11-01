import os
import pickle

class LessonDa:
    def __init__(self):
        self.filename = "data_access/data/lesson.dat"
        self.lesson_list = self.find_all()

    def save(self , lesson):
        self.lesson_list.append(lesson)
        file = open(self.filename , "wb")
        pickle.dump(self.lesson_list , file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            lesson_list = pickle.load(file)
            file.close()
            return lesson_list