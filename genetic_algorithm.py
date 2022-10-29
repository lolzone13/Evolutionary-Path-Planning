import random
import math
from path_map import Path_Map

course_map = Path_Map()


'''
Comments
 <----> is y
 up down is x




'''


class Individual:
    def __init__(self, num_possible_moves, moves=[], robot_height=3):
        self.moves = moves
        self.num_moves = len(moves)
        self.robot_height = robot_height

        if (self.num_moves == 0):
            # generate random moves

            for _ in range(num_possible_moves):
                self.moves.append(random.choice(self.possible_moves))

            self.num_moves = len(self.moves)

        self.fitness = self.fitness_function()

    def fitness_function(self):
        f = 0
        x, y = course_map.start
        tx, ty = course_map.end
        height = course_map.map[x][y]
        for m in range(self.num_moves):
            print(m, [x, y], end=" ")
            if (self.moves[m] == 'L'):
                if y > 0 and height + self.robot_height >= course_map.map[x][y-1]:
                    f = f + (course_map.map[x][y-1] - height + 1)
                    y = y - 1

            elif (self.moves[m] == 'U'):
                if x > 0 and height + self.robot_height >= course_map.map[x-1][y]:
                    f = f + (course_map.map[x-1][y] - height + 1)
                    x = x - 1

            elif (self.moves[m] == 'R'):
                if y < course_map.columns-1 and height + self.robot_height >= course_map.map[x][y+1]:
                    f = f + (course_map.map[x][y+1] - height + 1)
                    y = y + 1

            elif (self.moves[m] == 'D'):
                if x < course_map.rows-1 and height + self.robot_height >= course_map.map[x+1][y]:
                    f = f + (course_map.map[x+1][y] - height + 1)
                    x = x + 1

            if x == tx and y == ty:  # award the individual that gets to the final point
                f = f + len(self.moves)

            height = course_map.map[x][y]
            print(f)
        self.fitness = f
        return f


class Population:
    def __init__(self, population_size, num_possible_moves):
        self.population = []

        for _ in range(population_size):
            self.population.append(Individual(num_possible_moves))


    def average_fitness(self):
        total_fitness = 0
        for individual in self.population:
            total_fitness+=individual.fitness
        avg_fitness = total_fitness / len(self.population)

        return avg_fitness 

class Genetic_Algorithm:
    def __init__(self, population_size, iterations=10):
        self.population_size = population_size
        self.iterations = iterations

    def roulette_selection(self, fitness_values):
        total_fitness = sum(fitness_values)
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
            individual.moves[index] = random.choice('LURD')
        
        return individual

        
    def adaptive_mutation(self, population, individual, low_mut_prob, high_mut_prob):
        avg_fitness = population.average_fitness()

        mutation_probability = high_mut_prob if individual.fitness < avg_fitness else low_mut_prob

        return self.mutation(mutation_probability, individual)



