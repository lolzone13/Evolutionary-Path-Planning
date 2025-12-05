"""Fixed-length chromosome Genetic Algorithm with elitist selection."""

import random
import math
from path_map import Path_Map
from devtools import debug

from src.genetic_algorithm.base import GeneticAlgorithmBase
from src.individual import Individual
from src.population import Population

course_map = Path_Map()

'''
Comments
 <----> is y
 up down is x

'''


class GeneticAlgorithm(GeneticAlgorithmBase):
    """Genetic Algorithm with fixed-length chromosomes and elitist selection."""
    
    def __init__(self, population_size, num_possible_moves, iterations=1000):
        super().__init__(population_size, num_possible_moves, iterations)

    def core_function(self):
        tots = []
        population_object = Population(self.population_size, self.num_possible_moves)

        population = population_object.get_population()
        # selection, crossover, mutation
        next_generation = []
        for generation in range(self.iterations):

            fitness_values = population_object.get_fitnesses()
            # debug(fitness_values)
            for _ in range(population_object.population_size // 2):
                first_parent = population[self.roulette_selection(fitness_values)]
                second_parent = population[self.roulette_selection(fitness_values)]
        
                (first_child, second_child) = self.crossover(first_parent, second_parent)
                # debug("Children fitness", first_child.fitness, second_child.fitness)
                # debug("Children moves ", first_child.moves, second_child.moves)
                first_child = self.adaptive_mutation(population_object, first_child, 0, 0.8)
                second_child = self.adaptive_mutation(population_object, second_child, 0, 0.8)


                next_generation.append(first_child)
                next_generation.append(second_child)


            # survival of the fittest
            
            total_generation = population_object.population + next_generation

            sorted_gen = sorted(total_generation, key = lambda x : -x.fitness)

            population_object.population = sorted_gen[0:len(next_generation)]
            # best_individual = population_object.get_best_individual()
            # print(best_individual.fitness)
            print(population_object.average_fitness())
            next_generation = []

            if (generation == 5 or generation == 100 or generation == 200 or generation == 500 or generation == 1000 or generation == 1999):
                tots.append(population_object.get_best_individual())

        print("Final Population")
        population_object.print_population()

        print("best individual: ", end="")
        best_individual = population_object.get_best_individual()
        print(best_individual.moves, best_individual.fitness_function())
        self.values_at_iterations = tots
        return best_individual.moves
