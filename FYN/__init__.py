#init modules

from flask import Flask
from flask_login import LoginManager
import psycopg2

app = Flask(__name__)
app.config.from_object('config.Config')

login_manager = LoginManager()
login_manager.init_app(app)

import FYN.views
