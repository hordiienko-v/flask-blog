from app.db import db
from flask_login import UserMixin
from sqlalchemy import or_

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    bio = db.Column(db.String(100))
    password = db.Column(db.String())

    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def __init__(self, username, email, bio, password):
        self.username = username
        self.email = email
        self.bio = bio
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username_or_email(cls, username, email):
        return cls.query.filter(or_(cls.username==username, cls.email==email)).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
