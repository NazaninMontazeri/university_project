from  data_access.data.professor_da import ProfessorDa

class ProfessorBL:
    def __init__(self):
        self.professor_da = ProfessorDa()

    def save_professor(self, professor):
        all_professors = self.professor_da.find_all()
        for existing_professor in all_professors:
            if existing_professor.professor_id == professor.professor_id:
                raise ValueError(f"Professor ID {professor.professor_id} already exists!")
        self.professor_da.save(professor)
        return "Professor saved successfully."