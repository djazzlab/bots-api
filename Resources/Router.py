# Import API controllers
from Resources.CubeSolver.CubeSolverRgbToLab import CubeSolverRgbToLab

def InitializeRoutes(BotsAPI):
    # CubeSolver
    BotsAPI.add_resource(CubeSolverRgbToLab, '/bots-api/cube-solver/rgb-to-lab/<int:Red>/<int:Green>/<int:Blue>', endpoint = 'rgb_to_lab')