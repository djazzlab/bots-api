from flask_restful import Api
from Router import InitializeRoutes

# Create Flask APP
App = Flask(__name__)

# Init routes
InitializeRoutes(BotsAPI = Api(App))
