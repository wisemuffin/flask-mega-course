# you need to have a Python script at the top-level that defines the Flask application instance.
from app import create_app, db, cli
from app.models import User, Post

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go

app = create_app()
cli.register(app)

# app2 = dash.Dash(name='place1', sharing=True, server=app, url_base_pathname='/test1')
#
# app2.layout = html.Div([
#         html.H1('This is a test1')
#     ])

# app.shell_context_processor decorator registers the function as a shell context function.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
