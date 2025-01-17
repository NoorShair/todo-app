from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)
    completed = db.Column(db.Boolean, default=False)
