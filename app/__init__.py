from flask import Flask
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("blog-secret", "secret")

from app.routes import public_routes, private_routes

from app.models.user import User
from app.models.post import Post

if __name__ == "__main__":
    from app.db import db
    from flask_login import LoginManager
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "/sign-in"
    login_manager.init_app(app)

    @app.template_filter("format_date")
    def format_date(value, format="%H:%M %d.%m.%y"):
        return value.strftime(format)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.run(port=5000, debug=True)
