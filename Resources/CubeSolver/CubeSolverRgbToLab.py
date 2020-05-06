# API Imports
from flask_restful import reqparse as ReqParser
from flask_restful import Resource as APIResource

# Colormath
from colormath.color_conversions import convert_color as ConvertColor
from colormath.color_objects import sRGBColor, LabColor

# Parse arguments in the request body
ArgsParser = ReqParser.RequestParser()
ArgsParser.add_argument(
    'red',
    help = 'Red code of the RGB color to convert',
    required = True,
    type = int
)
ArgsParser.add_argument(
    'green',
    help = 'Green code of the RGB color to convert',
    required = True,
    type = int
)
ArgsParser.add_argument(
    'blue',
    help = 'Blue code of the RGB color to convert',
    required = True,
    type = int
)

class CubeSolverRgbToLab(APIResource):
    def get(self):
        try:
            Args = ArgsParser.parse_args()
            Red = Args['red']
            Green = Args['green']
            Blue = Args['blue']

            if Red < 0 or Red > 255:
                return {
                    'Message': 'Red integer should be greater or equal to 0 and lesser or equal to 255'
                }, 500
            elif Green < 0 or Green > 255:
                return {
                    'Message': 'Green integer should be greater or equal to 0 and lesser or equal to 255'
                }, 500
            elif Blue < 0 or Blue > 255:
                return {
                    'Message': 'Blue integer should be greater or equal to 0 and lesser or equal to 255'
                }, 500
            else:
                Lab = ConvertColor(
                    sRGBColor(Red, Green, Blue, True),
                    LabColor
                )
                LabTuple = Lab.get_value_tuple()

                return {
                    'Lab': {
                        'L': LabTuple[0],
                        'A': LabTuple[1],
                        'B': LabTuple[2]
                    }
                }
        except Exception as E:
            return {
                'Message': 'Exception while converting rgb color to lab: {}'.format(E)
            }, 500