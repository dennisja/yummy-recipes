from app import app
from app.decorators import disable_logout_access
from flask import render_template, request


@app.route("/")
@app.route("/index")
def home_page():
    return render_template("index.html")

@app.route("/login")
def login_user():
    pass

@app.route("/register",methods=["GET","POST"])
def register_user():
    form_data = request.form
    # //validate form form_data
    # if validation is passed
    # register_user user 
    # redirect user to login page while flashing a message
    return "{} {} {} {} {}".format(form_data["fname"], form_data["lname"],form_data["email"],form_data["password"],form_data["password_r"])