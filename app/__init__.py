from flask import Flask
from secret import secret_key

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = secret_key

from app.routes import public_routes, private_routes

from app.models.user import User
from app.models.post import Post

if __name__ == "__main__":
    print("__init__.py")
