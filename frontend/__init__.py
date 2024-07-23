from os import getenv
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

SECRET_KEY = getenv("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY

from . import routes


if __name__ == "__main__":
    app.run(debug=True)