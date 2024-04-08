from config import db

class Fitness_goal(db.Model):
    __tablename__ = 'fitness_goal'
    username = db.Column(db.Integer, primary_key=True)
    enter_goal = db.Column(db.String(200), nullable=False)
    user_name = db.Column(db.String, db.ForeignKey("user.username"))