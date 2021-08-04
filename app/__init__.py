from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.routes import public_routes

from app.models.user import User
from app.models.post import Post

if __name__ == "__main__":
    print("__init__.py")
