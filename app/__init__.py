from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

app = Flask(__name__)  # __name__ is a variable that is the name of module used
# list of FLASK EXTENSIONS that are initalised right after the application instance
app.config.from_object(Config)  # apply the Config class to the app so it inherits its properties
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # migration engine.
login = LoginManager(app)

# @login_required - can be added above a endpoint in routes.py if you only want logged in users to see
login = LoginManager(app)
login.login_view = 'login'

# at bottom becuase of circular imports (need flask extensions first)
from app import routes, models
