from model.student import Student
from  model.professor import Professor
from  model.lesson import Lesson
from  model.score import Score
from tools.validation import*

class SelectLesson :
    def __init__(self , student , professor , lesson ):
        self.student = student
        self.professor = professor
        self.lesson = lesson
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score_obj):
        Validator.score_validator(score_obj)
        self._score = score_obj

    def assign_score(self, score_obj):
        self.score = score_obj

    def __repr__(self):
        return (f"SelectLesson(\n"
                f"  student={self.student!r},\n"
                f"  professor={self.professor!r},\n"
                f"  lesson={self.lesson!r},\n"
                f"  score={self._score!r}\n"
                f")")