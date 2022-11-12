


import pygame
from path_map import Path_Map
from genetic_algorithm import Genetic_Algorithm





ga = Genetic_Algorithm(10 , 15,  1000)


path_string = ga.core_function()


map = Path_Map()



pygame.init()
screen = pygame.display.set_mode((700, 600))

black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)
blue = 	(0, 0, 255)
green = (0, 255, 0)
orange = (255, 165, 0)

# Create board with gridlines
board = pygame.Surface((550, 550))
board.fill(dark_grey)
for i in range(1, 11):
    pygame.draw.rect(board, grey, (0, -7 + i*55, 650, 4))
    pygame.draw.rect(board, grey, (-7 + i*55, 0, 4, 650))

# Create object
object1 = pygame.Surface((50, 50))
object1.fill(dark_grey)
pygame.draw.circle(object1, red, (25, 25), 25)

# start and end, start - green, end - orange
end = map.end
start = map.start
pygame.draw.circle(board, green, (start[0]*55 + 25,start[1]*55 + 25), 25)
pygame.draw.circle(board, orange, (end[0]*55 + 25,end[1]*55 + 25), 25)
# pygame.draw.circle(object1, green, (start[0]*55 + 25,start[1]*55 + 25), 25)


x, y = start
done = False
clock = pygame.time.Clock()

screen.fill(black)

font = pygame.font.SysFont("Arial", 30)
moves = path_string


def add_numbers():
    mp = map.generate_map()

    for i in range(len(mp)):
        for j in range(len(mp[0])):
            ft = font.render(str(mp[i][j]), True, blue)
            screen.blit(ft, (105 + i*55, 20 + j*55))


for i in moves:
    
    # Clear the screen   

    # Draw board
    screen.blit(board, (105, 20))

    


    # Draw objects
    screen.blit(object1, (105 + x*55, 20 + y*55))

    # img = font.render("2", True, blue)
    # screen.blit(img, (105, 20))

    add_numbers()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         x = (x - 1) % 10
        #     if event.key == pygame.K_RIGHT:
        #         x = (x + 1) % 10
        #     if event.key == pygame.K_UP:
        #         y = (y - 1) % 10
        #     if event.key == pygame.K_DOWN:
        #         y = (y + 1) % 10


    if done:
        break
    if (i == 'L'):
        if (x > 0):
            x-=1
    elif (i == 'D'):
        if (y < map.rows - 1):
            y+=1
    elif (i == 'U'):
        if (y > 0):
            y-=1
    elif (i == 'R'):        
        if (x < map.columns - 1):
            x+=1


    pygame.time.wait(1000)
    # Update the screen
    clock.tick()
    pygame.display.flip()


done = False
while not done:
    # Clear the screen
    

    # Draw board
    screen.blit(board, (105, 20))

    


    # Draw objects
    screen.blit(object1, (105 + x*55, 20 + y*55))
    pygame.time.wait(500)
    add_numbers()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = (x - 1) % 10
            if event.key == pygame.K_RIGHT:
                x = (x + 1) % 10
            if event.key == pygame.K_UP:
                y = (y - 1) % 10
            if event.key == pygame.K_DOWN:
                y = (y + 1) % 10
    clock.tick()
    pygame.display.flip()