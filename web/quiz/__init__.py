from flask import Flask
from .data import db_session

app = Flask(__name__)
app.config.from_object("quiz.config.Config")
from .routes import *

db_session.global_init(app.config['SQLALCHEMY_DATABASE_URL'])
