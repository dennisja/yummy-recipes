from flask import session,render_template

from functools import wraps


def disable_logout_access(func):
    """
    :param func: The function object of the decorated function
    :return:
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wraps the code to check whether a user is logged in
        :return:
        """
        if "logged_in" in session:
            return func(*args, **kwargs)  # call the decorated function
        return render_template("index.html")

    return wrapper