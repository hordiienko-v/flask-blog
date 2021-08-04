from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/about")
def about():
    return render_template("about.html")
