# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    #instantiate Player object and store it in a variable
    player = Player(x, y)
       

    while True:
        #check for window being closed by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill screen area in black
        screen.fill(000)

        #insert rotate player functionality
        player.update(dt)

        #draw player here
        player.draw(screen)   

        
        

        pygame.display.flip()

        #limit framrate to 60fps
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()