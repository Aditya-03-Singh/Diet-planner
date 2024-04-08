from config import db


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    bmi = db.relationship('BMI', backref='user')
    macros = db.relationship('Macros', backref='user')
    water_rem = db.relationship('Water_rem', backref='user')
    plans = db.relationship('Plans', backref='user')
    fitness_goal = db.relationship('Fitness_goal', backref='user')

