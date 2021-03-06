# Import API controllers
from Resources.CubeSolver.CubeSolverLabsDistance import CubeSolverLabsDistance
from Resources.CubeSolver.CubeSolverRgbToLab import CubeSolverRgbToLab

def InitializeRoutes(BotsAPI):
    # CubeSolver
    BotsAPI.add_resource(CubeSolverLabsDistance, '/bots-api/cube-solver/labs-distance', endpoint = 'labs_distance')
    BotsAPI.add_resource(CubeSolverRgbToLab, '/bots-api/cube-solver/rgb-to-lab', endpoint = 'rgb_to_lab')