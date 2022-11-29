# Objective function for minimization

import random
from devtools import debug

from path_map import Path_Map

course_map = Path_Map()

# Robot_hieght = bipedal threshold height reachable


class Individual:
    def __init__(self, num_possible_moves, moves=[], robot_height=3):
        self.moves = moves
        self.possible_moves = ['L', 'U', 'R', 'D']
        self.num_moves = len(moves)
        self.robot_height = robot_height
        self.num = num_possible_moves
        self.max_row = course_map.rows-1
        self.max_column = course_map.columns-1

        # if (self.num_moves == 0):
        #     # generate random moves

        #     for _ in range(num_possible_moves):
        #         self.moves.append(random.choice(self.possible_moves))

        #     self.num_moves = len(self.moves)

        self.fitness = self.fitness_function()

    def fitness_function(self):
        
        def relu(x):
            return (max(0, x))

        hard_pen1 = -10000
        hard_pen2 = -10

        f = 0
        x, y = course_map.start
        tx, ty = course_map.end
        height = course_map.map[x][y]

        for m in range(self.num_moves):


            # debug(course_map.map[x][y])
            if (self.moves[m] == 'L'):
                if y > 0 and height + self.robot_height >= course_map.map[x][y-1]:
                    f = f + self.num * \
                        (relu(course_map.map[x][y-1] - height)) + \
                        hard_pen2 * (((tx-x))**2+ ((ty-y+1))**2)
                    y = y - 1   
                elif y == 0:
                    f += hard_pen1
                elif height + self.robot_height <= course_map.map[x][y-1]:
                    f += hard_pen2 * \
                        (
                            (relu(height-course_map.map[x][y-1])))**2 + ((tx-x))**2+((ty-y+1))**2
                # y = y - 1
            elif (self.moves[m] == 'D'):
                if x < self.max_row and height + self.robot_height >= course_map.map[x+1][y]:
                    f = f + self.num * \
                        (relu(course_map.map[x+1][y] - height)) + \
                        hard_pen2 * (((tx-x-1)**2)+((ty-y)**2))
                    x = x + 1
                elif x == self.max_row:
                    f += hard_pen1
                elif height + self.robot_height <= course_map.map[x+1][y]:
                    f += hard_pen2 * \
                        (
                            (relu(height-course_map.map[x+1][y])))**2 + ((tx-x-1))**2+((ty-y))**2
                
            elif (self.moves[m] == 'R'):
                if y < self.max_column and height + self.robot_height >= course_map.map[x][y+1]:
                    f = f + self.num * \
                        (relu(course_map.map[x][y+1] - height)) + \
                        hard_pen2 * (((tx-x)**2)+((ty-y-1)**2))
                    y = y + 1
                elif y == self.max_column:
                    f += hard_pen1
                elif height + self.robot_height <= course_map.map[x][y+1]:
                    f += hard_pen2 * \
                        (
                            (relu(height-course_map.map[x][y+1])))**2 + ((tx-x))**2+((ty-y-1))**2
                
            elif (self.moves[m] == 'U'):
                if x > 0 and height + self.robot_height >= course_map.map[x-1][y]:
                    f = f + self.num * \
                        (relu(course_map.map[x-1][y] - height)) + \
                        hard_pen2 * (((tx-x+1))**2+((ty-y))**2)
                    x = x - 1
                elif x == 0:
                    f += hard_pen1
                elif height + self.robot_height <= course_map.map[x-1][y]:
                    f += hard_pen2 * \
                        (
                            (relu(height-course_map.map[x-1][y])))**2 + ((tx-x+1))**2+((ty-y))**2
                
            if x == tx and y == ty:  # award the individual that gets to the final point
                f += 10000 * (len(self.moves) - m) # reaching earlier is better
    
       
                # # experimental stuff
                # self.fitness = f
                # height = course_map.map[x][y]
   
                # return f
                
            
            # x = x%(self.max_row + 1)
            # y = y%(self.max_column + 1)
            height = course_map.map[x][y]

            # debug(m, f)
    
        self.fitness = f
        # debug(self.moves, self.fitness)
        return f

    def append_move(self, move):
        self.moves.append(move)
        self.num_moves += 1
        # print(self.moves, "append")

    def delete_move(self, index):
        removed_ele = self.moves.pop(index)
        self.num_moves -= 1
        # print(self.moves, "delete")

class Population:
    def __init__(self, population_size, num_possible_moves):
        self.population = []
        self.population_size = population_size
        for _ in range(population_size):
          
            new_moves = []

            for _ in range(num_possible_moves):
                new_moves.append(random.choice(['U', 'L', 'R', 'D']))
                # debug(new_moves, _)
            
            self.population.append(Individual(num_possible_moves, moves=new_moves))
       

        debug("Population: {}".format(num_possible_moves))
        self.print_population()

    def average_fitness(self):
        total_fitness = 0
        for individual in self.population:
            total_fitness+=individual.fitness_function()
        avg_fitness = total_fitness / len(self.population)

        return avg_fitness 

    def get_adjusted_fitnesses(self):
        fitnesses = []

        for i in self.population:
            fitnesses.append(i.fitness_function())

        min_fitness = min(fitnesses)

        for i in range(len(fitnesses)):
            fitnesses[i] -= min_fitness
        return fitnesses

    def get_fitnesses(self):
        fitnesses = []

        for i in self.population:

            fitnesses.append(i.fitness_function())

        return fitnesses

    def get_population(self):
        return self.population

    def print_population(self):
        for i in self.population:
            print(i.moves)
    
    def get_best_individual(self):
        best_individual = self.population[0]
        
        for individual in self.population:
            if individual.fitness_function() > best_individual.fitness_function():
                best_individual = individual
        return best_individual

    