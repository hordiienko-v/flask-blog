from app import app
from flask import render_template, request, redirect
from app.models.user import User

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    data = request.form
    if request.method == "POST":
        if User.find_by_username(data['username']):
            return render_template("sign_up.html", error="Username is already taken")
        elif any(v.isspace() or not v for v in request.form.values()):
            return render_template("sign_up.html", error="Empty field is not allowed")
        else:
            user = User(**data)
            user.save_to_db()
            return render_template("sign_up.html", success="User has been created")
    return render_template("sign_up.html")

@app.route("/about")
def about():
    return render_template("about.html")
