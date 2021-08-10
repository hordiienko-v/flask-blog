from app import app
from flask import render_template, request, redirect
from app.models.user import User
from app.models.post import Post
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@app.errorhandler(404)
def page_not_found(e):
    return render_template("basic_templates/errors/404.html"), 404

@app.route("/")
def home():
    posts = Post.get_last_twenty()
    return render_template("home.html", posts=posts)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    data = request.form
    if request.method == "POST":
        if any(v.isspace() or not v for v in request.form.values()):
            return render_template("sign_up.html", error="Empty field is not allowed")
        elif User.find_by_username_or_email(data['username'], data['email']):
            return render_template("sign_up.html", error="Username or email is already taken")
        else:
            user = User(username=data["username"], email=data["email"],
                password=generate_password_hash(data["password"], method="sha256"),
                bio='')
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
        if any(v.isspace() or not v for v in request.form.values()):
            return render_template("sign_in.html", error="Empty field is not allowed")
        elif user and check_password_hash(user.password, data["password"]):
            login_user(user, remember=remember)
            return redirect("/")
        elif user:
            return render_template("sign_in.html", error="Incorrect password")
        else:
            return render_template("sign_in.html", error="User does not exist")
    return render_template("sign_in.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        data = request.form

        post = Post(**data, timestamp=datetime.now(), author_id=current_user.get_id())
        post.save_to_db()

        return render_template("create_post.html", success="Post created")
    return render_template("create_post.html")

@app.route("/<int:user_id>/posts")
def posts(user_id):
    user = User.find_by_id(user_id)
    if user:
        posts = user.posts.all()
        return render_template("posts.html", username=user.username, user_id=user.id, posts=posts)
    return render_template("basic_templates/errors/404.html"), 404

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.find_by_id(post_id)
    if post:
        return render_template("post.html", post=post)
    return render_template("basic_templates/errors/404.html"), 404
