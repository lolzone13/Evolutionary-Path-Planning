from devtools import debug
from path_map import Path_Map
from population import Individual
from genetic_algorithm_var import Genetic_Algorithm_Var
from genetic_algorithm import Genetic_Algorithm
from visualizations import visualize_map
from new_population import Population

ind = Individual(10)
ga = Genetic_Algorithm(5,5, 2)


p = [3, 4, 2, 1, 7, 9]
# print(ga.roulette_selection(p))
path_string = ga.core_function()
visualize_map(path_string)
# print(ind.fitness)