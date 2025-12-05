from devtools import debug
from path_map import Path_Map
from src.individual import Individual
from src.genetic_algorithm import GeneticAlgorithm, GeneticAlgorithmVar





ga = GeneticAlgorithm(10 , 15,  1000)

moves = ['U', 'R', 'R', 'R', 'R', 'R', 'L', 'R', 'U', 'L', 'U', 'D', 'R', 'D', 'L']
# print(visualize_map(moves))
ind = Individual(15, moves).fitness_function()
# debug(ind)
# path_string = ga.core_function()


