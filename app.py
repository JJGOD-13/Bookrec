import os
import flask
from cs50 import SQL

from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

# configure application
app = flask.Flask(__name__)


# configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


@app.route("/")
def hello_world():
    return "<p>Hello, world!<p>"
