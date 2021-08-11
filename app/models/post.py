from app.db import db
from sqlalchemy import desc

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # author = db.relationship('User')

    def __init__(self, title, body, timestamp, author_id):
        self.title = title
        self.body = body
        self.timestamp = timestamp
        self.author_id = author_id

    def json(self):
        res = {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%H:%M %d.%m.%y"),
            "author_id": self.author_id,
            "author_username": self.author.username
        }
        return res

    @classmethod
    def get_last_five(cls):
        return list(cls.query.order_by(desc(Post.timestamp)).limit(5).all())

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_title(cls, title):
        return list(cls.query.filter_by(title=title))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
