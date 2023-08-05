from flask import redirect, render_template, request, session
from functools import wraps

# From CS50 "helpers.py" in the finance assignment.
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def is_even(value):
    if value % 2 == 0:
        return True
    return False