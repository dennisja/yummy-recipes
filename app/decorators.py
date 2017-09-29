from flask import session,render_template,flash,redirect

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
        
        flash("You cannot access this page without logging in","errors")
        return redirect("/")

    return wrapper