from flask import Flask
from flask_restful import Api
from Resources.Router import InitializeRoutes

# Create Flask APP
App = Flask(__name__)
API = Api(
    App,
    description = 'A simple API for hard operations to be done by EV3 robots',
    version = '1.0',
    title = 'Bots API'
)

ApiNS = API.namespace('bots', description = 'Bots hard operations')

# Init routes
InitializeRoutes(BotsAPI = API)
