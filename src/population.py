"""Population class managing a collection of individuals."""

import random
from devtools import debug

from src.individual import Individual
from src.constants import MOVES


class Population:
    def __init__(self, population_size, num_possible_moves):
        self.population = []
        self.population_size = population_size
        for _ in range(population_size):
          
            new_moves = []

            for _ in range(num_possible_moves):
                new_moves.append(random.choice(MOVES))
                # debug(new_moves, _)
            
            self.population.append(Individual(num_possible_moves, moves=new_moves))
       

        debug("Population: {}".format(num_possible_moves))
        self.print_population()

    def average_fitness(self):
        total_fitness = 0
        for individual in self.population:
            total_fitness += individual.fitness
        avg_fitness = total_fitness / len(self.population)

        return avg_fitness 

    def get_adjusted_fitnesses(self):
        fitnesses = []

        for i in self.population:
            fitnesses.append(i.fitness)

        min_fitness = min(fitnesses)

        for i in range(len(fitnesses)):
            fitnesses[i] -= min_fitness
        return fitnesses

    def get_fitnesses(self):
        fitnesses = []

        for i in self.population:
            fitnesses.append(i.fitness)

        return fitnesses

    def get_population(self):
        return self.population

    def print_population(self):
        for i in self.population:
            print(i.moves)
    
    def get_best_individual(self):
        best_individual = self.population[0]
        
        for individual in self.population:
            if individual.fitness > best_individual.fitness:
                best_individual = individual
        return best_individual
