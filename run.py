from app import app
from flask_login import LoginManager
from app.models.user import User


if __name__ == "__main__":
    from app.db import db
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "/sign-in"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(port=5000, debug=True)
