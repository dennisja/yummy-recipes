class UserNotFoundException(Exception):
    pass


class NullUserError(Exception):
    pass


class Users():
    def __init__(self):
        self.users = {
            "1": {
                "firstname": "Jjagwe",
                "lastname": "Dennis",
                "email": "dennisjjagwe@gmail.com",
                "password": "password"
            },
            "2": {
                "firstname": "Walukagga",
                "lastname": "Patrick",
                "email": "patrick.py@gmail.com",
                "password": "mypassword"
            }
        }

    def add_user(self, user):
        if user:
            self.users[str(len(self.users) + 1)] = user
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
            raise NullUserError("The user you are trying to remove doesnot exist")

    @property
    def get_all_users(self):
        return self.users


class User():
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    @property
    def user_details(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password
        }

    def __repr__(self):
        return "<User {} {}>".format(self.firstname, self.lastname)

class Recipe():
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def __repr__(self):
        return "<Recipe {}>".format(self.name)



class RecipesList(list):
    def __init__(self):
        list.__init__([])
        self.extend([Recipe("chips and chicken","This will make you love eating. Its cool and awesome","Break fast"),
        Recipe("Banana Crumb Muffins","Keep calm, You got to love banana Test it and see","Quick and Easy")])

