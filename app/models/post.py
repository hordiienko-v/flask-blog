from app.db import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    author = db.relationship('User')

    def __init__(self, body, author_id):
        self.body = body
        self.author_id = author_id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_title(cls, title):
        return list(cls.query.filter_by(title=title))
