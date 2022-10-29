import random
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
        self.possible_moves = ['U', 'L', 'R', 'D']
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



class Genetic_Algorithm:
    def __init__(self, population_size, iterations=10):
        self.population_size = population_size
        self.iterations = iterations

    # def crossover(self):
