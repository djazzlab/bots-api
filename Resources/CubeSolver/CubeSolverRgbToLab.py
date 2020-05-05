from flask import jsonify as JsonResponse
from flask_restful import Resource as APIResource

class CubeSolverRgbToLab(APIResource):
    def get(self, Red, Green, Blue):
        return JsonResponse({
            'Red': Red,
            'Green': Green,
            'Blue': Blue
        })