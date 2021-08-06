from app import app
from flask import render_template, request, redirect
from app.models.user import User
from flask_login import login_user, logout_user, login_required, current_user

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

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    data = request.form
    if data.get("remember"):
        remember = True
    else:
        remember = False
    if request.method == "POST":
        user = User.find_by_username(data["username"])
        if user and user.password == data["password"]:
            login_user(user, remember=remember)
            return redirect("/")
        elif user:
            return render_template("sign_in.html", error="Incorrect password")
        elif any(v.isspace() or not v for v in request.form.values()):
            return render_template("sign_in.html", error="Empty field is not allowed")
        else:
            return render_template("sign_in.html", error="User does not exist")
    return render_template("sign_in.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/sign-in")

@app.route("/about")
def about():
    return render_template("about.html")
