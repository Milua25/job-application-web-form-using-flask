from app import db

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    date = db.Column(db.DateTime, nullable=False)
    occupation = db.Column(db.String(80), nullable=False)
