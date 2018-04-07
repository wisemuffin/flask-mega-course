# you need to have a Python script at the top-level that defines the Flask application instance.
from app import app, db
from app.models import User, Post


# app.shell_context_processor decorator registers the function as a shell context function.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
