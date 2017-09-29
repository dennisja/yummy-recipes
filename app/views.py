from app import app
from app.decorators import disable_logout_access
from app.validator import Validate
from flask import render_template, request, flash, redirect, url_for, session
from app.simulators import User, Users, Recipe, RecipesList

app.secret_key = "I Love coding"


@app.route("/")
@app.route("/index")
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login_user():
    session["logged_in"] = True
    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    if "logged_in" in session:
        session.pop("logged_in")
    return redirect(url_for("home_page"))


@app.route("/home")
@disable_logout_access  # custom decorator
def home():
    return render_template("dashboard.html", recipes=RecipesList(),user_is_logged_in = True)


@app.route("/register", methods=["GET", "POST"])
def register_user():
    form_data = request.form
    # validate form form_data
    validate = Validate()

    validation_errors = validate.validate_data(form_data, {
        "fname": {
            "required": True,
            "min": 4,
            "max": 20,
            "no_number": True
        },
        "lname": {
            "required": True,
            "min": 4,
            "max": 20,
            "no_number": True,
        },
        "email": {
            "required": True,
            "max": 100,
            "min": 10
        },
        "password": {
            "required": True,
            "min": 8,
            "max": 20
        },
        "c_password": {
            "matches": "password"
        }
    })
    # if validation is passed
    if not validation_errors:
        flash("You have successfully registered and you can now login", "success")
    else:
        for validation_error in validation_errors:
            flash((validation_error), "register_errors")
    return redirect(url_for("home_page"))
