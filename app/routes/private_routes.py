from app import app
from flask import render_template, request, redirect
from app.models.user import User
from app.models.post import Post
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/sign-in")

@login_required
@app.route("/profile")
def profile():
    return render_template("profile.html", user=current_user)

@login_required
@app.route("/change_bio", methods=["POST"])
def change_bio():
    new_bio = request.get_json()["bio"]
    current_user.bio = new_bio
    current_user.save_to_db()

    return {"message": "OK"}

@login_required
@app.route("/change_email", methods=["POST"])
def change_email():
    new_email = request.get_json()["email"]
    current_user.email = new_email
    current_user.save_to_db()

    return {"message": "OK"}
