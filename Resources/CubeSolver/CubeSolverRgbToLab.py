# API Imports
from flask import jsonify as JsonResponse
from flask import make_response as MakeResponse
from flask_restful import Resource as APIResource

# Colormath
from colormath.color_objects import sRGBColor, LabColor

class CubeSolverRgbToLab(APIResource):
    def get(self, Red, Green, Blue):
        if Red < 0 or Red > 255:
            return MakeResponse(
                JsonResponse({
                    'Message': 'Red integer should be greater or equal to 0 and lesser or equal to 255'
                }),
                500
            )
        elif Green < 0 or Green > 255:
            return MakeResponse(
                JsonResponse({
                    'Message': 'Green integer should be greater or equal to 0 and lesser or equal to 255'
                }),
                500
            )
        elif Blue < 0 or Blue > 255:
            return MakeResponse(
                JsonResponse({
                    'Message': 'Blue integer should be greater or equal to 0 and lesser or equal to 255'
                }),
                500
            )
        else:
            try:
                return MakeResponse(
                    JsonResponse({
                        'Lab': ConvertColor(
                            sRGBColor(Red, Green, Blue, True),
                            LabColor
                        )
                    }),
                    200
                )
            except Exception as E:
                return MakeResponse(
                    JsonResponse({
                        'Message': 'Exception while converting rgb color to lab: {}'.format(E)
                    }),
                    500
                )