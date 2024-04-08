from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
from models.user import User
from models.bmi import BMI
from models.water_rem import Water_rem

from models.fitness_goal import Fitness_goal
from models.macros import Macros


load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATINS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        
        @app.route('/signup', methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)

            user = User.query.filter_by(username=data['username']).first()

            if user is None:

                new_user = User(
                    username = data['username'],
                    password = data['password'],
                    email = data['email']
                )

                db.session.add(new_user)
                db.session.commit()
                return jsonify(msg = "user signup is done successfully")
            else:
                return jsonify(msg = "User already exists")

        @app.route('/water_checker', methods = ['POST'])
        def water_checker():
            username= request.args.get('username')
            user = User.query.filter_by(Username=username).first()
            print(username)
            waterchecker = request.get_json()
            new_water = Water(
                water_intake= waterchecker["water_intake"],
                user_name= user.username
            )
            db.session.add(new_water)
            db.session.commit()
            print((height/(weight**2)))
            return jsonify(msg="we recieved your water details, but for normal functioning please have 8 glasses of water")

            

        db.create_all()
        db.session.commit()

        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)