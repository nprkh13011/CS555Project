from config import db

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eeg_af3 = db.Column(db.Float, nullable = False)
    eeg_t7 = db.Column(db.Float, nullable = False)
    eeg_Pz = db.Column(db.Float, nullable = False)
    eeg_T8 = db.Column(db.Float, nullable = False)
    eeg_AF4 = db.Column(db.Float, nullable = False)
    true_false = db.Column(db.Integer, unique=False, nullable=False)
    

    def to_json(self):
        return{
            "id": self.id,
            "eeg_af3": self.eeg_af3,
            "eeg_t7": self.eeg_t7,
            "eeg_Pz": self.eeg_Pz,
            "eeg_T8": self.eeg_T8,
            "eeg_AF4": self.eeg_AF4,
            "trueFalse": self.true_false
        }