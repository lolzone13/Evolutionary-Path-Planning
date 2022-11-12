import random
import math
from path_map import Path_Map
from devtools import debug

course_map = Path_Map()

from new_population import Individual, Population

'''
Comments
 <----> is y
 up down is x

'''




class Genetic_Algorithm:
    def __init__(self, population_size, num_possible_moves, iterations=1000):
        self.iterations = iterations
        self.num_possible_moves = num_possible_moves
        self.population_size = population_size

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
        child2.fitness = child1.fitness_function()

        
        return (child1, child2)


    def mutation(self, mutation_probability, individual):


        for index in range(individual.num_moves):
            p = random.random()

            if (p < mutation_probability):
                individual.moves[index] = random.choice(individual.possible_moves)
    
        return individual

        
    def adaptive_mutation(self, population, individual, low_mut_prob, high_mut_prob):
        avg_fitness = population.average_fitness()

        mutation_probability = high_mut_prob if individual.fitness < avg_fitness else low_mut_prob

        return self.mutation(mutation_probability, individual)


    def core_function(self):
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
                first_child = self.adaptive_mutation(population_object, first_child, 0.8, 0.8)
                second_child = self.adaptive_mutation(population_object, second_child, 0.8, 0.8)


                next_generation.append(first_child)
                next_generation.append(second_child)


            # survival of the fittest
            
            total_generation = population_object.population + next_generation

            sorted_gen = sorted(total_generation, key = lambda x : -x.fitness)

            population_object.population = sorted_gen[0:len(next_generation)]
            next_generation = []

        print("Final Population")
        population_object.print_population()

        print("best individual: ", end="")
        best_individual = population_object.get_best_individual()
        print(best_individual.moves, best_individual.fitness)
        return best_individual.moves



