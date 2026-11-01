from business_logic.professor_bl import ProfessorBL
from model.professor import Professor

class ProfessorController:
    def __init__(self):
        self.professor_bl = ProfessorBL()

    def save_professor(self, name, family, national_id, phone, salary, professor_id, lesson):
        try:
            prof = Professor(name, family, national_id, phone, salary, professor_id, lesson)
            self.professor_bl.save_professor(prof)
            return True, "Professor saved successfully."
        except Exception as e:
            return False, f"Save Failed: {e}"

    def find_all_professors(self):
        try:
            professors = self.professor_bl.professor_da.find_all()
            return True, professors
        except Exception as e:
            return False, f"Error fetching professors: {e}"