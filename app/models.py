from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    email = db.Column(db.String, primary_key=True)
    requests_left = db.Column(db.Integer, default=50)

class EuromillionsResult(db.Model):
    __tablename__ = 'euromillions'

    date = db.Column(db.String, primary_key=True)
    numbers = db.Column(db.String, nullable=False)   
    stars = db.Column(db.String, nullable=False)     
    prizes = db.Column(db.Text, nullable=True)       
