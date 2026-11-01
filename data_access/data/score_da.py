import os
import pickle

class ScoreDa:
    def __init__(self):
        self.filename = "data_access/data/score.dat"
        self.score_list = self.find_all()

    def save(self , score):
        self.score_list.append(score)
        file = open(self.filename , "wb")
        pickle.dump(self.score_list , file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            score_list = pickle.load(file)
            file.close()
            return score_list