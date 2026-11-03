import os
import pickle


class SelectLessonDa:
    def __init__(self):
        self.filename = "data_access/data/select_lesson.dat"
        self.select_lesson_list = self.find_all()

    def save(self, select_lesson):
        self.select_lesson_list.append(select_lesson)
        file = open(self.filename, "wb")
        pickle.dump(self.select_lesson_list, file)
        file.close()

    def update(self, select_lesson):

        found = False
        for i, s in enumerate(self.select_lesson_list):
            if getattr(s.student, "student_id", None) == select_lesson.student.student_id:
                self.select_lesson_list[i] = select_lesson
                found = True
                break

        if not found:
            self.select_lesson_list.append(select_lesson)

        file = open(self.filename, "wb")
        pickle.dump(self.select_lesson_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            select_lesson_list = pickle.load(file)
            file.close()
            return select_lesson_list