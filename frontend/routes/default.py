from .. import app
from flask import render_template
from flask_login import current_user
from .login import login, register



@app.get("/")
def index():
    return render_template("index.html", user=current_user)