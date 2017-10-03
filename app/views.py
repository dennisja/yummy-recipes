from app import app
from app.decorators import disable_logout_access
from app.validator import Validate
from flask import render_template, request, flash, redirect, url_for, session
from app.simulators import User, Users, Recipe, RecipesDict, RecipeCategory, RecipeCategoryDict

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
    recipes = RecipesDict(str(session["logged_in"]))
    return render_template("dashboard.html", recipes=recipes.fetch_user_recipes().values(), user_is_logged_in=True, user=my_user)


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
            flash("Email \"{}\" is already in use".format(
                form_data["email"]), "register_errors")
        else:
            users = Users()
            user = User(len(users.get_all_users(
            )) + 1, form_data["fname"], form_data["lname"], form_data["email"], form_data["password"])
            users.add_user(user)
            users.save_users(users.get_all_users())
            flash("You have successfully registered and you can now login", "success")
    else:
        for validation_error in validation_errors:
            flash((validation_error), "register_errors")
    return redirect(url_for("home_page"))


@app.route("/recipes")
@disable_logout_access
def get_recipes():
    users = Users()
    my_user = users.get_all_users()[session["logged_in"]]
    recipes = RecipesDict(session["logged_in"]).fetch_user_recipes()
    return render_template("recipes.html", recipes= recipes.values(), user_is_logged_in=True, user=my_user)


@app.route("/recipe/<recipe_id>",methods = ["POST","GET"])
@disable_logout_access
def get_recipe(recipe_id):
    recipes = RecipesDict(session["logged_in"])
    form_data = request.form
    if not form_data:
        return render_template("edit-recipe.html", recipe = recipes.fetch_user_recipes()[str(recipe_id)])
    else:
        new_recipe = Recipe(recipe_id, form_data["name"], form_data["description"], form_data["category"],session["logged_in"])
        recipes.edit_recipe(session["logged_in"],recipe_id,new_recipe.recipe_details())

        return render_template("recipes.html",
            recipes = recipes.fetch_user_recipes().values(), 
            user=Users().get_all_users()[session["logged_in"]],
            user_is_logged_in = True)


@app.route("/delete-recipe/<recipe_id>",methods=["POST","GET"])
@disable_logout_access
def delete_recipe(recipe_id):
    recipes = RecipesDict(session["logged_in"])
    available_recipes = recipes.fetch_user_recipes()
    available_recipes.pop(str(recipe_id))
    return render_template("recipes.html",
            recipes = available_recipes.values(), 
            user=Users().get_all_users()[session["logged_in"]],
            user_is_logged_in = True)



@app.route("/add-recipe", methods=["POST","GET"])
@disable_logout_access
def add_recipe():
    form_data = request.form
    if form_data:
        # validate recipe
        validator = Validate()
        validation_errors = validator.validate_data(form_data,{
            "name":{
                "required":True,
                "min":5,
                "max":200
            },
            "description":{
                "max":200
            }
        })

        if not validation_errors:
            recips = RecipesDict(session["logged_in"])
            existing_recipes = recips.fetch_user_recipes()
            recipe = Recipe(len(existing_recipes)+1, form_data["name"], form_data["description"], form_data["category"],session["logged_in"])
            recips.add_recipe(recipe.recipe_details(),session["logged_in"])
            users = Users()
            user = users.get_all_users()[session["logged_in"]]
            return render_template("recipes.html", 
                    recipes = recips.fetch_user_recipes().values(),
                    user_is_logged_in = True,
                    user = user
                    )
        return str(request.form)
    return render_template("add-recipe.html", page_title="Add a Recipe",user_is_logged_in=True, user = Users().get_all_users()[session["logged_in"]])


@app.route("/add-recipe-category")
@disable_logout_access
def add_recipe_category():
    return render_template("add-recipe-category.html",page_title="Add Recipe Category")


@app.route("/edit-recipe/<recipe_id>")
@disable_logout_access
def edit_recipe(recipe_id):
    return "Edit {}".format(recipe_id)


@app.route("/edit-recipe-category/<recipe_cat_id>")
@disable_logout_access
def edit_recipe_category(recipe_cat_id):
    return "Edit {}".format(recipe_cat_id)
