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
            'lab1_lightness',
            location = 'form',
            store_missing = False,
            type = float
        )
        self.__ArgsParser.add_argument(
            'lab1_dim_a',
            location = 'form',
            store_missing = False,
            type = float
        )
        self.__ArgsParser.add_argument(
            'lab1_dim_b',
            location = 'form',
            store_missing = False,
            type = float
        )
        self.__ArgsParser.add_argument(
            'lab2_lightness',
            location = 'form',
            store_missing = False,
            type = float
        )
        self.__ArgsParser.add_argument(
            'lab2_dim_a',
            location = 'form',
            store_missing = False,
            type = float
        )
        self.__ArgsParser.add_argument(
            'lab2_dim_b',
            location = 'form',
            store_missing = False,
            type = float
        )

    def get(self):
        try:
            Args = self.__ArgsParser.parse_args(strict = True)

            LAB1 = tuple()
            LAB2 = tuple()

            if 'lab1_lightness' in Args:
                LAB1 += (Args['lab1_lightness'],)
            else:
                raise Exception('Your request body must have a value for the lab1_lightness argument')

            if 'lab1_dim_a' in Args:
                LAB1 += (Args['lab1_dim_a'],)
            else:
                raise Exception('Your request body must have a value for the lab1_dim_a argument')
            
            if 'lab1_dim_b' in Args:
                LAB1 += (Args['lab1_dim_b'],)
            else:
                raise Exception('Your request body must have a value for the lab1_dim_b argument')

            if 'lab2_lightness' in Args:
                LAB2 += (Args['lab2_lightness'],)
            else:
                raise Exception('Your request body must have a value for the lab2_lightness argument')

            if 'lab2_dim_a' in Args:
                LAB2 += (Args['lab2_dim_a'],)
            else:
                raise Exception('Your request body must have a value for the lab2_dim_a argument')
            
            if 'lab2_dim_b' in Args:
                LAB2 += (Args['lab2_dim_b'],)
            else:
                raise Exception('Your request body must have a value for the lab2_dim_b argument')

            self.__LABColor1 = LabColor(
                lab_l = float(LAB1[0]),
                lab_a = float(LAB1[1]),
                lab_b = float(LAB1[2])
            )

            self.__LABColor2 = LabColor(
                lab_l = float(LAB2[0]),
                lab_a = float(LAB2[1]),
                lab_b = float(LAB2[2])
            )

            return {
                'Distance': DeltaCie2000(self.__LABColor1, self.__LABColor2)
            }
        except Exception as E:
            return {
                'Message': str(E)
            }, 500