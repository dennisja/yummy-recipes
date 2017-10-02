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
    form_data = request.form
    users = Users()
    available_users = users.get_all_users()
    if form_data["email"] in available_users and available_users[form_data["email"]]["password"] == form_data["password"]:
        session["logged_in"] = form_data["email"]
        return redirect(url_for("home"))
    flash("Invalid username and password combination", "login_errors")
    return render_template("index.html")


@app.route("/logout")
def logout():
    if "logged_in" in session:
        session.pop("logged_in")
    return redirect(url_for("home_page"))


@app.route("/home")
@disable_logout_access  # custom decorator
def home():
    users = Users()
    my_user = users.get_all_users()[session["logged_in"]]
    return render_template("dashboard.html", recipes=RecipesList(), user_is_logged_in=True, user=my_user)


@app.route("/register", methods=["GET", "POST"])
def register_user():
    form_data = request.form
    users = Users()
    available_users = users.get_all_users()
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
        if form_data["email"] in available_users:
            flash("Email \"{}\" is already in use".format(form_data["email"]), "register_errors")
        else:
            users = Users()
            user = User(len(users.get_all_users())+1, form_data["fname"], form_data["lname"], form_data["email"], form_data["password"])
            users.add_user(user)
            users.save_users(users.get_all_users())
            flash("You have successfully registered and you can now login", "success")
    else:
        for validation_error in validation_errors:
            flash((validation_error), "register_errors")
    return redirect(url_for("home_page"))
