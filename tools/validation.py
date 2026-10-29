import re


class Validator:
    @staticmethod
    def name_validator(name):
        if not re.match(r"^[a-zA-Z]{2,30}$", name):
            raise ValueError("Invalid Name")

    @staticmethod
    def family_validator(family):
        if not re.match(r"^[a-zA-Z]{2,40}$" , family):
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
            raise ValueError("Invalid salary")
        if salary < 0 :
            raise ValueError("Salary cannot be negative.")