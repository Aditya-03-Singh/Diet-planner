from config import db

class BMI(db.Model):
    __tablename__ = 'bmi'
    username = db.Column(db.String, primary_key=True)
    # username = db.Column(db.String(200), nullable=False)
    height = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.String(200), nullable=False)
    # how to get bmi
    user_name = db.Column(db.String, db.ForeignKey("user.username"))