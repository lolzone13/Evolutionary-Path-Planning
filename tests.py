import pytest

from path_map import Path_Map
from population import Individual
from genetic_algorithm import Genetic_Algorithm


ind = Individual(10, 'DDDDDRRUUR')
ga = Genetic_Algorithm()


p = [3, 4, 2, 1, 7, 9]
# print(ga.roulette_selection(p))
ga.core_function()

# print(ind.fitness)