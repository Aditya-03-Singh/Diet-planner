from config import db

class Water_rem(db.Model):
    __tablename__ = 'water_rem'
    username = db.Column(db.String, primary_key=True)
    # username = db.Column(db.String(200), nullable=False)
    water_intake = db.Column(db.integer(200), nullable=False)
    # weight = db.Column(db.String(200), nullable=False)
    # how to get bmi
    user_name = db.Column(db.String, db.ForeignKey("user.username"))