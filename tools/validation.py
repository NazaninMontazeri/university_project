import re
from datetime import datetime

class Validator:
    @staticmethod
    def name_validator(name):
        if not isinstance(name , str) or not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name")

    @staticmethod
    def family_validator(family):
        if not isinstance(family , str) or not re.match(r"^[a-zA-Z]{2,40}$" , family):
            raise ValueError("Invalid Family")

    @staticmethod
    def national_id_validator(national_id):
        if not isinstance(national_id , str) or not re.match(r"^[0-9]{10}$" , national_id):
            raise ValueError("Invalid National Id")

    @staticmethod
    def phone_validator(phone):
        if not isinstance(phone , str) or not re.match(r"^[0-9]{11}$" , phone):
            raise ValueError("Invalid Phone")

    @staticmethod
    def salary_validator(salary):
        if not isinstance(salary , (int , float)) :
            raise ValueError("Invalid Salary")
        if salary < 0 :
            raise ValueError("Salary cannot be negative.")

    @staticmethod
    def professor_id_validator(professor_id):
        if not isinstance(professor_id , int) :
            raise ValueError("Invalid Professor id")
        if professor_id <= 0:
            raise ValueError("Professor id cannot be negative or zero")

    @staticmethod
    def lesson_validator(lesson):
        if not isinstance(lesson , str)  or not re.match(r"^[a-zA-Z]{2,40}$" , lesson):
            raise ValueError("Invalid Lesson")

    @staticmethod
    def student_id_validator(student_id):
        if not isinstance(student_id , int) :
            raise ValueError("Invalid Student id")
        if student_id <= 0 :
            raise ValueError("Student id cannot be negative or zero")

    @staticmethod
    def field_of_study_validator(field_of_study):
        if not isinstance(field_of_study , str) or not re.match(r"^[a-zA-Z]{2,40}$" , field_of_study):
            raise ValueError("Invalid Field of study")

    @staticmethod
    def name_lesson_validator(name_lesson):
        if not isinstance(name_lesson , str) or not re.match(r"^[a-zA-Z]{2,40}$" , name_lesson):
            raise ValueError("Invalid Name lesson")

    @staticmethod
    def units_validator(units):
        if not isinstance(units , int):
            raise ValueError("Invalid Units")
        if units <= 0:
            raise ValueError("Units cannot be negative or zero")

    @staticmethod
    def lesson_code_validator(lesson_code):
        if not isinstance(lesson_code , int) :
            raise ValueError("Invalid Lesson code")
        if lesson_code <= 0:
            raise ValueError("Lesson code cannot be negative or zero")

    @staticmethod
    def score_date_validator(score_date):
        if not isinstance(score_date , str):
            raise ValueError("Invalid Score date")

        try:
            datetime.strptime(score_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format: {score_date}. Correct format: YYYY-MM-DD")