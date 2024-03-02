#import modules
import pygame, sys

class fruit:
    def __init__(self):
        #create x and y position
        #draw a square
        self.x = 5
        self.y = 4

#set game screen and frame per second
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


#set game screen to close and 60 frames per second
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((175,215,70))
    pygame.display.update()
    clock.tick(60)