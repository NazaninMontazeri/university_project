from model.score import Score
from data_access.data.score_da import ScoreDa


class ScoreController:
    def __init__(self):
        self.score_da = ScoreDa()

    def save_score(self, score_date, score_value):
        try:
            new_score = Score(score_date, score_value)
            self.score_da.save(new_score)
            return True, "Score saved successfully."
        except Exception as e:
            return False, f"Error: {e}"

    def find_all_score(self):
        try:
            scores = self.score_da.find_all()
            return True, scores
        except Exception as e:
            return False, f"Error: {e}"