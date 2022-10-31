import random
import math
from path_map import Path_Map

course_map = Path_Map()

from population import Individual, Population

'''
Comments
 <----> is y
 up down is x

'''




class Genetic_Algorithm:
    def __init__(self, population_size, iterations=10):
        self.population_size = population_size
        self.iterations = iterations

    def roulette_selection(self, fitness_values):
        total_fitness = sum(fitness_values)
        # minimum_fitness = min(fitness_values)
        probabilities = [math.ceil((v/total_fitness) * 100)
                         for v in fitness_values]

        selection_weights = []
        accumulated_sum = 0

        for p in probabilities:
            accumulated_sum += p
            selection_weights.append(accumulated_sum)

        # spin roulette wheel and generate solution
        p = random.randint(0, selection_weights[-1])
        for i in range(len(selection_weights)):
            if (selection_weights[i] >= p):
                return i

    def crossover(self, parent1, parent2):
        num = random.randint(0, parent1.num_moves-1)
        child1 = Individual(parent1.num_moves,
                            parent1.moves[0:num] + parent2.moves[num:])
        child2 = Individual(parent2.num_moves,
                            parent2.moves[0:num] + parent1.moves[num:])

        return (child1, child2)


    def mutation(self, mutation_probability, individual):
        p = random.random()

        if (p < mutation_probability):
            index = random.randint(0,individual.num_moves-1)
            individual.moves[index] = random.choice(individual.possible_moves)
        
        return individual

        
    def adaptive_mutation(self, population, individual, low_mut_prob, high_mut_prob):
        avg_fitness = population.average_fitness()

        mutation_probability = high_mut_prob if individual.fitness < avg_fitness else low_mut_prob

        return self.mutation(mutation_probability, individual)


    def core_function(self):
        population = Population(10, 10).get_population()

        # selection, crossover, mutation
        next_generation = []
        for generation in range(self.iterations):

            fitness_values = population.get_fitnesses()
            
            for _ in range(population.population_size // 2):
                first_parent = self.roulette_selection(fitness_values)
                second_parent = self.roulette_selection(fitness_values)

                (first_child, second_child) = self.crossover(first_parent, second_parent)

                first_child = self.adaptive_mutation(population, first_child, 0.4, 0.8)
                second_child = self.adaptive_mutation(population, second_child, 0.4, 0.8)


                next_generation.append(first_child)
                next_generation.append(second_child)


            population.population = next_generation
            next_generation = []

        print("Final Population")
        print(population.population)

        print("best individual: ", end="")
        print(population.get_best_individual())



