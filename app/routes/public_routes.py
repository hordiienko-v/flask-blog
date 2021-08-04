from app import app

@app.route("/")
def home():
    return "Home page"

@app.route("/sign-up")
def sign_up():
    return "Sign-up"

@app.route("/about")
def about():
    return "About"
