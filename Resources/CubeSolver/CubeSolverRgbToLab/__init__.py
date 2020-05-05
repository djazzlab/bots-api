from flask import jsonify as JsonResponse
from flask_restful import Resource

class CubeSolverRgbToLab(Resource):
    def get(self, Red, Green, Blue):
        return JsonResponse({
            'hello': 'world'
        })