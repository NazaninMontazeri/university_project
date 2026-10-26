from tools.validation import *

class Person :
    def __init__(self , name , family , national_id , phone ):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.name_validator(name)
        self.__name = name

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self , family):
        Validator.family_validator(family)
        self.__family = family

    @property
    def national_id(self):
        return self.__national_id

    @national_id.setter
    def national_id(self , national_id):
        #Validator.national_id_validator(national_id)
        self.__national_id = national_id

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self , phone):
        #Validator.phone_validator(phone)
        self.__phone = phone

    def __repr__(self):
        return f"Person(name = {self.name} , family = {self.family} , natinal_id = {self.national_id} , phone = {self.phone})"

    def to_tuple(self):
        return (self.name , self.family , self.national_id , self.phone)