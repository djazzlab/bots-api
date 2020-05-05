from flask import Flask
from flask import jsonify as JsonResponse

App = Flask(__name__)

@App.route('/')
def Hello():
    return JsonResponse([
        {
            'hello': 'world'
        },
        {
            'hello2': 'world2'
        }
    ])

App.run(host = '0.0.0.0')