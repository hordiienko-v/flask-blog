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
    if request.get_json()["bio"].length <= 100:
        new_bio = request.get_json()["bio"]
        current_user.bio = new_bio
        current_user.save_to_db()

    return {"message": "OK"}

@login_required
@app.route("/change_email", methods=["POST"])
def change_email():
    new_email = request.get_json()["email"]
    if User.find_by_email(new_email):
        return {"message": "Email is already taken"}
    current_user.email = new_email
    current_user.save_to_db()

    return {"message": "OK"}

@login_required
@app.route("/change_password", methods=["POST"])
def change_password():
    data = request.get_json()
    print('check: ', check_password_hash(current_user.password, data["old"]))
    print('old: ', data["old"])
    print('new: ', data["new"])
    if check_password_hash(current_user.password, data["old"]):
        if data["old"] == data["new"]:
            return {"message": "New password cannot be the same"}
        current_user.password = generate_password_hash(data["new"], method="sha256")
        current_user.save_to_db()
        return {"message": "OK"}
    return {"message": "Incorrect password"}

@login_required
@app.route("/delete_post", methods=["DELETE"])
def delete_post():
    data = request.get_json()
    post = current_user.posts.filter(Post.id==data["post_id"]).first()
    if post:
        post.delete_from_db()
    return {"message": "OK"}
