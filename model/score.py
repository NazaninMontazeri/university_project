from tools.validation import *

class Score :
    def __init__(self , score_date , score_value):
        self.score_date = score_date
        self.score_value = score_value

    @property
    def score_date(self):
        return self.__score_date

    @score_date.setter
    def score_date(self , score_date):
        Validator.score_date_validator(score_date)
        self.__score_date = score_date

    @property
    def score_value(self):
        return self.__score_value

    @score_value.setter
    def score_value(self , score_value):
        Validator.score_value_validator(score_value)
        self.__score_value = score_value

    def __repr__(self):
        return f"Score(score_date = {self.score_date} , score_value = {self.score_value})"

    def to_tuple(self):
        return self.score_date , self.score_value

    def get_result(self):
        if self.score_value >= 10 :
             return f"Pass by {self.score_value}"
        else:
            return f"Fail by {self.score_value}"