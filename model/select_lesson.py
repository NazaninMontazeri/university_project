from  model.score import Score
from tools.validation import*

class SelectLesson :
    def __init__(self , student , professor , lesson ):

        from model.student import Student
        from model.professor import Professor
        from model.lesson import Lesson

        self.student = student
        self.professor = professor
        self.lesson = lesson
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score_obj):
        Validator.score_validator(self._score)
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

    def to_tuple(self):
        return self.student , self.professor , self.lesson , self._score