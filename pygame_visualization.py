
# import os
# import sys
# import random
# import pygame
 
 
# BLUE = (0, 0, 255)

# # Class for the orange dude
# class Player(object):
    
#     def __init__(self):
#         self.rect = pygame.Rect(32, 32, 16, 16)
 
#     def move(self, dx, dy):
        
#         # Move each axis separately. Note that this checks for collisions both times.
#         if dx != 0:
#             self.move_single_axis(dx, 0)
#         if dy != 0:
#             self.move_single_axis(0, dy)
    
#     def move_single_axis(self, dx, dy):
        
#         # Move the rect
#         self.rect.x += dx
#         self.rect.y += dy
 
#         # If you collide with a wall, move out based on velocity
#         for wall in walls:
#             if self.rect.colliderect(wall.rect):
#                 if dx > 0: # Moving right; Hit the left side of the wall
#                     self.rect.right = wall.rect.left
#                 if dx < 0: # Moving left; Hit the right side of the wall
#                     self.rect.left = wall.rect.right
#                 if dy > 0: # Moving down; Hit the top side of the wall
#                     self.rect.bottom = wall.rect.top
#                 if dy < 0: # Moving up; Hit the bottom side of the wall
#                     self.rect.top = wall.rect.bottom
 
# # Nice class to hold a wall rect
# class Wall(object):
    
#     def __init__(self, pos):
#         walls.append(self)
#         self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
 
# # Initialise pygame
# os.environ["SDL_VIDEO_CENTERED"] = "1"
# pygame.init()
 
# # Set up the display
# pygame.display.set_caption("Get to the red square!")
# screen = pygame.display.set_mode((320, 240))
 
# clock = pygame.time.Clock()
# walls = [] # List to hold the walls
# player = Player() # Create the player
 
# # Holds the level layout in a list of strings.
# # level = [
# #     "WWWWWWWWWWWWWWWWWWWW",
# #     "W                  W",
# #     "W         WWWWWW   W",
# #     "W   WWWW       W   W",
# #     "W   W        WWWW  W",
# #     "W WWW  WWWW        W",
# #     "W   W     W W      W",
# #     "W   W     W   WWW WW",
# #     "W   WWW WWW   W W  W",
# #     "W     W   W   W W  W",
# #     "WWW   W   WWWWW W  W",
# #     "W W      WW        W",
# #     "W W   WWWW   WWW   W",
# #     "W     W    E   W   W",
# #     "WWWWWWWWWWWWWWWWWWWW",
# # ]
 
# level = [
#             [0, 0, 0, 0, 0, 0, 0, 8, 8, 0, ],
#             [0, 4, 4, 0, 0, 0, 0, 0, 0, 0, ],
#             [0, 4, 0, 4, 0, 0, 0, 1, 1, 0, ],
#             [0, 0, 0, 6, 6, 0, 0, 3, 3, 0, ],
#             [0, 4, 0, 6, 6, 0, 0, 5, 5, 0, ],
#             [0, 2, 3, 4, 4, 0, 0, 7, 7, 0, ],
#             [0, 4, 7, 2, 2, 6, 0, 8, 8, 0, ],
#             [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, ],
#             [0, 0, 4, 4, 4, 0, 0, 0, 0, 0, ],
#             [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, ],
#         ]

# # Parse the level string above. W = wall, E = exit
# x = y = 0
# for row in level:
#     for col in row:
#         # if col == "W":
#         #     Wall((x, y))
#         # if col == "E":
#         #     end_rect = pygame.Rect(x, y, 16, 16)

#         font = pygame.font.SysFont(None, 24)
#         img = font.render(col, True, BLUE)
#         screen.blit(img, (16, 16))
#         x += 16
#     y += 16
#     x = 0
 
# running = True
# while running:
    
#     clock.tick(60)
    
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
#         if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
#             running = False
 
#     # Move the player if an arrow key is pressed
#     key = pygame.key.get_pressed()
#     if key[pygame.K_LEFT]:
#         player.move(-2, 0)
#     if key[pygame.K_RIGHT]:
#         player.move(2, 0)
#     if key[pygame.K_UP]:
#         player.move(0, -2)
#     if key[pygame.K_DOWN]:
#         player.move(0, 2)
 
#     # Just added this to make it slightly fun ;)
#     if player.rect.colliderect(end_rect):
#         pygame.quit()
#         sys.exit()
 
#     # Draw the scene
#     screen.fill((0, 0, 0))
#     for wall in walls:
#         pygame.draw.rect(screen, (255, 255, 255), wall.rect)
#     pygame.draw.rect(screen, (255, 0, 0), end_rect)
#     pygame.draw.rect(screen, (255, 200, 0), player.rect)
#     # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
#     pygame.display.flip()
#     clock.tick(360)
 
# pygame.quit()


import pygame



from path_map import Path_Map

map = Path_Map()



pygame.init()
screen = pygame.display.set_mode((800, 700))

black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)
blue = 	(0, 0, 255)

# Create board with gridlines
board = pygame.Surface((650, 650))
board.fill(dark_grey)
for i in range(1, 11):
    pygame.draw.rect(board, grey, (0, -7 + i*55, 650, 4))
    pygame.draw.rect(board, grey, (-7 + i*55, 0, 4, 650))

# Create object
object1 = pygame.Surface((100, 100))
object1.fill(dark_grey)
pygame.draw.circle(object1, red, (25, 25), 25)

x, y = (0, 0)
done = False
clock = pygame.time.Clock()

screen.fill(black)

font = pygame.font.SysFont("Arial", 30)
moves = ['U', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'U', 'D', 'R', 'R']


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

  
    if (i == 'U'):
        if (x > 0):
            x-=1
    elif (i == 'R'):
        if (y < map.columns - 1):
            y+=1
    elif (i == 'L'):
        if (y > 0):
            y-=1
    elif (i == 'D'):
        
        if (x < map.rows - 1):
            x+=1

    pygame.time.wait(200)
    # Update the screen
    clock.tick()
    pygame.display.flip()



while not done:
    # Clear the screen
    

    # Draw board
    screen.blit(board, (105, 20))

    


    # Draw objects
    screen.blit(object1, (105 + x*55, 20 + y*55))

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