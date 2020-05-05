from flask import jsonify as JsonResponse
from flask import Response
from flask_restful import Resource as APIResource

class CubeSolverRgbToLab(APIResource):
    def get(self, Red, Green, Blue):
        if Red < 0 or Red > 255:
            return Response(
                'Red integer should be greater or equal to 0 and lesser or equal to 255'
                mimetype = 'application/json',
                status = 500
            )
        elif Green < 0 or Green > 255:
            return Response(
                'Green integer should be greater or equal to 0 and lesser or equal to 255'
                mimetype = 'application/json',
                status = 500
            )
        elif Blue < 0 or Blue > 255:
            return Response(
                'Blue integer should be greater or equal to 0 and lesser or equal to 255'
                mimetype = 'application/json',
                status = 500
            )
        else:
            return Response(
                JsonResponse({
                    'Red': Red,
                    'Green': Green,
                    'Blue': Blue
                }),
                mimetype = 'application/json',
                status = 200
            )