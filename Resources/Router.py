# Import API controllers
from CubeSolver import CubeSolverRgbToLab

def InitializeRoutes(BotsAPI):
    # CubeSolver
    BotsAPI.add_resource(CubeSolverRgbToLab, '/cube-solver/rgb-to-lab/<int:Red>/<int:Green>/<int:Blue>')