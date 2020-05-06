# API Imports
from flask_restful import reqparse as ReqParser
from flask_restful import Resource as APIResource

# Colormath
from colormath.color_conversions import convert_color as ConvertColor
from colormath.color_objects import sRGBColor, LabColor

class CubeSolverRgbToLab(APIResource):
    __ArgsParser = None
    
    def __init__(self):
        # Parse arguments in the request body
        self.__ArgsParser = ReqParser.RequestParser(bundle_errors = True)
        self.__ArgsParser.add_argument(
            'red',
            help = 'Red argument is required and must be an integer greater or equal to 0 and lesser or equal to 255',
            required = True,
            type = int
        )
        self.__ArgsParser.add_argument(
            'green',
            help = 'Green argument is required and must be an integer greater or equal to 0 and lesser or equal to 255',
            required = True,
            type = int
        )
        self.__ArgsParser.add_argument(
            'blue',
            help = 'Blue  argument is required and must be an integer greater or equal to 0 and lesser or equal to 255',
            required = True,
            type = int
        )

    def get(self):
        try:
            Args = self.__ArgsParser.parse_args()
            Red = Args['red']
            Green = Args['green']
            Blue = Args['blue']

            if Red < 0 or Red > 255:
                raise Exception('Red integer should be greater or equal to 0 and lesser or equal to 255')
            elif Green < 0 or Green > 255:
                raise Exception('Green integer should be greater or equal to 0 and lesser or equal to 255')
            elif Blue < 0 or Blue > 255:
                raise Exception('Blue integer should be greater or equal to 0 and lesser or equal to 255')
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
                'Message': str(E)
            }, 500