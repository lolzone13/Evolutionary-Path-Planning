"""Base class for Genetic Algorithm implementations."""

import random
import math
from abc import ABC, abstractmethod

from src.individual import Individual
from src.population import Population


class GeneticAlgorithmBase(ABC):
    """Abstract base class for genetic algorithm variants."""
    
    def __init__(self, population_size, num_possible_moves, iterations=1000):
        self.iterations = iterations
        self.num_possible_moves = num_possible_moves
        self.population_size = population_size
        self.values_at_iterations = []

    def roulette_selection(self, fitness_values):
        total_fitness = sum(fitness_values)
  
        # minimum_fitness = min(fitness_values)
        num_fitness = len(fitness_values)
        minimum_fitness = min(fitness_values)
        probabilities = [math.ceil(((v-minimum_fitness)/(total_fitness - num_fitness*minimum_fitness + 1)) * 100)
                         for v in fitness_values]

        selection_weights = []

        
        # accumulated_sum = 0
        # print(probabilities, sum(probabilities))
        # for p in probabilities:
        #     accumulated_sum += p
        #     selection_weights.append(accumulated_sum)
        # print(selection_weights)
        
        selection_weights = probabilities
        if (sum(selection_weights) == 0):
            selection_weights[0] = 1
        return random.choices([i for i in range(0,len(fitness_values))], weights=selection_weights, k=1)[0]
        
        # spin roulette wheel and generate solution
        # p = random.randint(0, max(probabilities))
        # for i in range(len(selection_weights)):
        #     if (selection_weights[i] >= p):
        #         return i

    def crossover(self, parent1, parent2):
        num = random.randint(0, parent1.num_moves-1)
        # debug("Parent Moves", parent1.moves, parent2.moves)
        # l1 = parent1.moves[0:num] + parent2.moves[num:]
        # l2 = parent2.moves[0:num] + parent1.moves[num:]

        # debug("Parents moves exchanged: ",l1, l2)
        child1 = Individual(parent1.num_moves,
                            parent1.moves[0:num] + parent2.moves[num:])
        child2 = Individual(parent2.num_moves,
                            parent2.moves[0:num] + parent1.moves[num:])
        child1.fitness = child1.fitness_function()
        child2.fitness = child2.fitness_function()

        
        return (child1, child2)

    def mutation(self, mutation_probability, individual):
        for index in range(individual.num_moves):
            p = random.random()

            if (p < mutation_probability):
                individual.moves[index] = random.choice(individual.possible_moves)
    
        return individual

    def adaptive_mutation(self, population, individual, low_mut_prob, high_mut_prob):
        # avg_fitness = population.average_fitness()
        avg_fitness = population.get_best_individual().fitness
        mutation_probability = high_mut_prob if individual.fitness < avg_fitness else low_mut_prob

        return self.mutation(mutation_probability, individual)

    @abstractmethod
    def core_function(self):
        """Run the genetic algorithm. Must be implemented by subclasses."""
        pass
