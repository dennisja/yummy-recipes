from app import app
from app.decorators import disable_logout_access
from flask import render_template


@app.route("/")
@app.route("/index")
def home_page():
    return render_template("index.html")

@app.route("/login")
def login_user():
    pass

@app.route("/register")
@disable_logout_access
def register_user():
    pass