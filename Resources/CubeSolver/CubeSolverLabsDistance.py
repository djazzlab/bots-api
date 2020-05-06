# API Imports
from flask_restful import reqparse as ReqParser
from flask_restful import Resource as APIResource

# Colormath
from colormath.color_diff import delta_e_cie2000 as DeltaCie2000
from colormath.color_objects import LabColor

class CubeSolverLabsDistance(APIResource):
    __ArgsParser = None
    __LABColor1 = None
    __LABColor2 = None
    
    def __init__(self):
        # Parse arguments in the request body
        self.__ArgsParser = ReqParser.RequestParser()
        self.__ArgsParser.add_argument(
            'lab1',
            help = 'First LAB color to calculate the distance',
            required = True,
            type = dict
        )
        self.__ArgsParser.add_argument(
            'lab2',
            help = 'Second LAB color to calculate the distance',
            required = True,
            type = dict
        )

    def get(self):
        try:
            Args = self.__ArgsParser.parse_args()
            print(Args)
        except Exception as E:
            return {
                'Message': 'Exception while converting rgb color to lab: {}'.format(E)
            }, 500