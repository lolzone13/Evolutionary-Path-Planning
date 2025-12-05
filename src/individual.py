# Objective function for minimization

import random

from path_map import Path_Map
from src.constants import MOVES, HARD_PENALTY_BOUNDARY, HARD_PENALTY_DISTANCE, TARGET_REACHED_MULTIPLIER, DEFAULT_ROBOT_HEIGHT

course_map = Path_Map()

# Robot_hieght = bipedal threshold height reachable


class Individual:
    def __init__(self, num_possible_moves, moves=[], robot_height=DEFAULT_ROBOT_HEIGHT):
        self.moves = moves
        self.possible_moves = MOVES
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

        hard_pen1 = HARD_PENALTY_BOUNDARY
        hard_pen2 = HARD_PENALTY_DISTANCE

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
                f += TARGET_REACHED_MULTIPLIER * (len(self.moves) - m) # reaching earlier is better
    
       
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
