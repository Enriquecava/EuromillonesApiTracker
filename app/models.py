from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    email = db.Column(db.String, primary_key=True)
    requests_left = db.Column(db.Integer, default=50)
