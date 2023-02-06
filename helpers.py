import os
import requests
import urllib.parse

import flask
import functools

def login_required(f):
    """Decorate routes to require login."""
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if flask.session.get("user_id") is None:
            return flask.redirect("/login")
        return f(*args, **kwargs)
    return decorated_function