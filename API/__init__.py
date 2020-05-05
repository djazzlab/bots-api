from flask import Flask

# Import controllers
from API.CubeSolver.Controllers import CubeSolver

# Create Flask APP
App = Flask(__name__)

# Declare controllers
App.register_blueprint(CubeSolver, url_prefix = '/cube-solver')
