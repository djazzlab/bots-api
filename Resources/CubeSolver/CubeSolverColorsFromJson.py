# API Imports
from flask_restful import reqparse as ReqParser
from flask_restful import Resource as APIResource

# Colormath
from colormath.color_conversions import convert_color as ConvertColor
from colormath.color_diff import delta_e_cie2000 as DeltaCie2000
from colormath.color_objects import sRGBColor, LabColor

class CubeSolverColorsFromJson(APIResource):
    __ArgsParser = None
    
    def __init__(self):
        # Parse arguments in the request body
        self.__ArgsParser = ReqParser.RequestParser()
        self.__ArgsParser.add_argument(
            'base_colors',
            location = 'json',
            store_missing = False,
            type = dict
        )
        self.__ArgsParser.add_argument(
            'scanned_colors',
            location = 'json',
            store_missing = False,
            type = dict
        )

    def get(self):
        try:
            Args = self.__ArgsParser.parse_args(strict = True)

            if 'base_colors' in Args:
                BaseColors = Args['base_colors']
            else:
                raise Exception('Your request body must have a json content for the base_colors argument')

            if 'scanned_colors' in Args:
                ScannedColors = Args['scanned_colors']
            else:
                raise Exception('Your request body must have a json content for the scanned_colors argument')

            AnalyzedSquares = {}
            for (SquarePosition, (RedCode, GreenCode, BlueCode)) in ScannedColors.items():
                Lab = ConvertColor(
                    sRGBColor(RedCode, GreenCode, BlueCode, True),
                    LabColor
                )

                CieData = []
                for (ColorShortName, LABColorCode) in BaseColors.items():
                    Distance = DeltaCie2000(
                        Lab,
                        LabColor(
                            lab_l = LABColorCode[0],
                            lab_a = LABColorCode[1],
                            lab_b = LABColorCode[2]
                        )
                    )

                    CieData.append((Distance, ColorShortName))
                
                CieData = sorted(CieData)
                if len(CieData) > 0:
                    AnalyzedSquares[SquarePosition] = CieData[0][1]

            return {
                'Result': AnalyzedSquares
            }
        except Exception as E:
            return {
                'Message': str(E)
            }, 500