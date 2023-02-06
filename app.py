import os
import flask
from cs50 import SQL
from helpers import login_required

from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

# configure application
app = flask.Flask(__name__)

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PerMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///people.db")


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
