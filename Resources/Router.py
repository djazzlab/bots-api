# Import API controllers
from Resources.CubeSolver import CubeSolverRgbToLab

def InitializeRoutes(BotsAPI):
    # CubeSolver
    BotsAPI.add_resource(CubeSolverRgbToLab, '/cube-solver/rgb-to-lab/<int:Red>/<int:Green>/<int:Blue>', endpoint = 'rgb_to_lab')