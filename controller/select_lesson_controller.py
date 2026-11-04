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


    def register_lesson(self, student_id, professor_id, lesson_code):
        try:

            try:
                student_id = int(student_id)
                professor_id = int(professor_id)
                lesson_code = int(lesson_code)
            except (ValueError, TypeError):
                return False, "student_id, professor_id and lesson_code must be integers"


            student = self.find_student_by_id(student_id)
            if not student:
                return False, "Student not found"

            professor = self.find_professor_by_id(professor_id)
            if not professor:
                return False, "Professor not found"

            lesson = self.find_lesson_by_code(lesson_code)
            if not lesson:
                return False, "Lesson not found"


            if student.select_lesson is not None:
                return False, "Student has already selected a lesson"


            if professor.professor_lesson != lesson.name_lesson:
                return False, (
                    f"Professor does not teach this lesson! "
                    f"(Professor teaches: '{professor.professor_lesson}', "
                    f"Lesson is: '{lesson.name_lesson}')"
                )


            new_reg = SelectLesson(student=student , professor=professor , lesson=lesson)


            student.choose_lesson(new_reg)


            self.select_lesson_da.save(new_reg)

            return True, "Lesson registered successfully."

        except ValueError as e:
            return False, f"Validation Error: {e}"
        except Exception as e:
            return False, f"Registration Failed: {e}"


    def submit_score(self, student_id, score_value, score_date):
        try:

            try:
                student_id = int(student_id)
            except (ValueError, TypeError):
                return False, "student_id must be an integer"

            try:
                score_value = float(score_value)
            except (ValueError, TypeError):
                return False, "score_value must be a number"

            student = self.find_student_by_id(student_id)
            if not student:
                return False, "Student not found"

            if student.select_lesson is None:
                return False, "Student has no selected lesson to score!"

            if student.select_lesson.score is not None:
                return False, "Business Error: Score has already been recorded!"

            new_score = Score( score_date=score_date , score_value=score_value)

            student.select_lesson.assign_score(new_score)

            self.score_da.save(new_score)

            self.select_lesson_da.update(student.select_lesson)

            result = new_score.get_result()
            return True, f"Score submitted. {result}"

        except ValueError as e:
            return False, f"Validation Error: {e}"
        except Exception as e:
            return False, f"Score Submission Failed: {e}"


    def find_student_by_id(self, student_id):
        student = None
        for s in self.student_da.find_all():
            if s.student_id == student_id:
                student = s
                break

        if not student:
            return None

        reg = None
        for r in self.select_lesson_da.find_all():
            if getattr(r.student, "student_id", None) == student_id:
                reg = r
                break

        student.select_lesson = reg
        return student

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

    def find_all_select_lesson(self):
        try:
            registers = self.select_lesson_da.find_all()
            return True, registers
        except Exception as e:
            return False, f"Error: {e}"