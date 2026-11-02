from model.select_lesson import SelectLesson
from model.score import Score
from data_access.data.student_da import StudentDa
from data_access.data.professor_da import ProfessorDa
from data_access.data.lesson_da import LessonDa
from data_access.data.select_lesson_da import SelectLessonDa
from data_access.data.score_da import ScoreDa

class SelectLessonController:
    def __init__(self):
        self.student_da = StudentDa()
        self.professor_da = ProfessorDa()
        self.lesson_da = LessonDa()
        self.score_da = ScoreDa()
        self.select_lesson_da = SelectLessonDa()

    def register_lesson(self , student_id , professor_id , lesson_code):
        try:
            student = self.find_student_by_id(student_id)
            professor = self.find_professor_by_id(professor_id)
            lesson = self.find_lesson_by_code(lesson_code)

            if not student:
                return False , "Student not found"

            if not professor:
                return False, "Professor not found"

            if not lesson:
                return False, "Lesson not found"

            if student.select_lesson is not None:
                return False, "Student has already selected a lesson"

            new_reg = SelectLesson(student , professor , lesson)
            self.select_lesson_da.save(new_reg)

            return True , "Lesson registered successfully."
        except Exception as e:
            return False, f"Registration Failed: {e}"

    def submit_score(self , student_id , score_value , score_date):
        try:
            student = self.find_student_by_id(student_id)
            if not student:
                return False , "Student not found"

            if student.selected_lesson is None :
                return False, "Student has no selected lesson to score!"
            if student.selected_lesson.score is not None:
                return False, "Business Error: Score has already been recorded!"

            new_score = Score(score_date, score_value)
            student.selected_lesson.score = new_score
            self.score_da.save(new_score)

            result = new_score.get_result()
            return True, f"Score submitted. {result}"

        except Exception as e:
            return False, f"Score Submission Failed: {e}"

    def find_student_by_id(self, student_id):
        for s in self.student_da.find_all():
            if s.student_id == student_id:
                return s
        return None

    def find_professor_by_id(self, professor_id):
        for p in self.professor_da.find_all():
            if p.professor_id == professor_id:
                return p
        return None

    def find_lesson_by_code(self, lesson_code):
        for l in self.lesson_da.find_all():
            if l.lesson_code == lesson_code:
                return l
        return None