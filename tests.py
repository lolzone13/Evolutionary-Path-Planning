from devtools import debug
from path_map import Path_Map

from genetic_algorithm_var import Genetic_Algorithm_Var
from genetic_algorithm import Genetic_Algorithm
from visualizations import visualize_map
from new_population import Individual




ga = Genetic_Algorithm(10 , 15,  1000)

# moves = ['U', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'U', 'D', 'R', 'R']
# print(visualize_map(moves))
# ind = Individual(15, moves).fitness_function()
# debug(ind)
path_string = ga.core_function()
visualize_map(path_string)

