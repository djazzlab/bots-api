from flask import jsonify as JsonResponse
from flask_restful import Resource as APIResource

class CubeSolverRgbToLab(APIResource):
    def get(Red, Green, Blue):
        return JsonResponse({
            'hello': 'world'
        })