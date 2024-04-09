from config import db

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    true_false = db.Column(db.Integer, unique=False, nullable=False)

    def to_json(self):
        return{
            "id": self.id,
            "trueFalse": self.true_false
        }