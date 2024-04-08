from config import db

class Macros(db.Model):
    __tablename__ = 'macros'
    username = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(200), nullable=False)
    protein = db.Column(db.String(200), nullable=False)
    carbs = db.Column(db.String(200), nullable=False)
    fats = db.Column(db.String(200), nullable=False)
    user_name = db.Column(db.String, db.ForeignKey("user.username"))