from app.db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    posts = db.relationship("Post", lazy="dynamic")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(self, _id):
        return cls.query.filter_by(id=_id).first()
