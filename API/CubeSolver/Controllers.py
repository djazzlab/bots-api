from flask import Blueprint
from flask import jsonify as JsonResponse

CubeSolver = Blueprint('CubeSolver', __name__)

@CubeSolver.route('/')
def Index():
    return JsonResponse({
        'hello': 'world'
    })