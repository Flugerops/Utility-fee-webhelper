from .. import app
from flask import render_template
from flask_login import current_user
from .login import login, register



@app.get("/")
def index():
    try:
        user = current_user.nickname
    except:
        user = None
        
    return render_template("index.html", user=user)