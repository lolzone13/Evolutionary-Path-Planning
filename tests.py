from devtools import debug
from path_map import Path_Map

from genetic_algorithm_var import Genetic_Algorithm_Var
from genetic_algorithm import Genetic_Algorithm
from visualizations import visualize_map
from new_population import Individual




ga = Genetic_Algorithm(10 , 20,  100)


p = [3, 4, 2, 1, 7, 9]
# print(ga.roulette_selection(p))
path_string = ga.core_function()
visualize_map(path_string)
# print(ind.fitness)

