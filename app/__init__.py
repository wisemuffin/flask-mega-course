from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail

app = Flask(__name__)  # __name__ is a variable that is the name of module used
# list of FLASK EXTENSIONS that are initalised right after the application instance
app.config.from_object(Config)  # apply the Config class to the app so it inherits its properties
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # migration engine.
# @login_required - can be added above a endpoint in routes.py if you only want logged in users to see
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

'''
e Mail Set up for debugging
- enable the email logger when the application is running without debug mode
- creates a SMTPHandler instance, sets its level so that it only reports errors and not warnings,
- informational or debugging messages, and finally attaches it to the app.logger object from Flask
'''
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

# at bottom becuase of circular imports (need flask extensions first)
from app import routes, models, errors
