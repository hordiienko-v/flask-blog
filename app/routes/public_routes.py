from app import app
from flask import render_template, request, redirect

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    data = request.form
    if request.method == "POST":
        if data['username'] == 'admin' and data['password'] == 'admin':
            return redirect("/")
        else:
            return render_template("sign_up.html", error="Incorrect login or password")
    return render_template("sign_up.html")

@app.route("/about")
def about():
    return render_template("about.html")
