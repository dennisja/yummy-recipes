import pickle


class UserNotFoundException(Exception):
    pass


class NullUserError(Exception):
    pass


class RecipeNotFoundError(Exception):
    pass


class Users():
    def __init__(self):
        self.users = self.read_users()

    def add_user(self, user):
        if user:
            self.users[user.email] = user.user_details
        else:
            raise NullUserError("Cannot add empty user")

    def get_user(self, user_id):
        if str(user_id) in self.users:
            return self.users[str(user_id)]
        else:
            raise UserNotFoundException("The requested user was not found")

    def delete_user(self, user_id):
        if str(user_id) in self.users:
            self.users.pop(str(user_id))
        else:
            raise NullUserError(
                "The user you are trying to remove doesnot exist")

    def save_users(self, users):
        """ Saves users data structure """
        with open("users.pickle", "wb") as users_file:
            pickle.dump(self.users, users_file)

    def read_users(self):
        """ Reads users data structure """
        with open("users.pickle", "rb") as users:
            all_users = pickle.load(users)
        return all_users

    def get_all_users(self):
        return self.users


class User():
    def __init__(self, id, firstname, lastname, email, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    @property
    def user_details(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password
        }

    def __repr__(self):
        return "<User {} {}>".format(self.firstname, self.lastname)


class Recipe():
    def __init__(self, recipe_id, name, description, category, owner):
        self.id = recipe_id
        self.name = name
        self.description = description
        self.category = category
        self.owner = owner

    def recipe_details(self):
        return {
            "id":  self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "owner": self.owner
        }

    def __repr__(self):
        return "<Recipe {}>".format(self.name)


class RecipeCategory():
    def __init__(self, recipe_id, name, owner):
        self.id = recipe_id
        self.name = name
        self.owner = owner

    def recipe_cat_details(self):
        return {
            "id": self.owner,
            "name": self.name,
            "owner": self.owner
        }

    def __repr__(self):
        return "<RecipeCategory {}>".format(self.name)


class RecipeCategoryDict():
    def __init__(self, user_email):
        self.recipes_category = self.__get_recipes_categories(user_email)

    def __get_recipes_categories(self, user_email):
        recipes_categories = {
            "dennisjjagwe@gmail.com": {
                "1": {
                    "id": 1,
                    "name": "Lunch",
                    "visible": 1,
                    "owner": "dennisjjagwe@gmail.com"
                },
                "2": {
                    "id": 2,
                    "name": "Break List",
                    "visible": 1,
                    "owner": "dennisjjagwe@gmail.com"
                }
            }
        }
        return recipes_categories[user_email]


class RecipesDict():
    def __init__(self, user_email):
        self.recipes = self.__get_user_recipes(user_email)
        self.all_recipes = self.read_recipes()

    def __get_user_recipes(self, user_email):
        recipes = self.read_recipes()
        if user_email in recipes:
            return recipes[user_email]
        else:
            return {}

    def add_recipe(self, recipe, user_email):
        if len(self.recipes):
            new_recipe_id = int(sorted([key for key in self.recipes.keys()])[-1]) + 1
        else:
            new_recipe_id = 1
        self.recipes[str(new_recipe_id)] = recipe
        self.save_all_recipes(self.recipes, user_email)

    def edit_recipe(self, user_email, recipe_id, new_recipe):
        if recipe_id in self.recipes:
            self.recipes[str(recipe_id)] = new_recipe
            self.save_all_recipes(self.recipes, user_email)
        else:
            raise RecipeNotFoundError("Recipe Not found")

    def fetch_user_recipes(self):
        return self.recipes

    def save_all_recipes(self, new_recipes, email):
        self.all_recipes[email] = new_recipes
        """ Saves recipes dictionary """
        with open("recipes.pickle", "wb") as recipes_:
            pickle.dump(self.all_recipes, recipes_)

    def read_recipes(self):
        """ Reads recipes dictionary """
        with open("recipes.pickle", "rb") as recipes:
            all_recipes = pickle.load(recipes)
        return all_recipes

class RecipesList(list):
    pass
