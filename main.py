# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #pygame.time.Clock
    clock = pygame.time.Clock()
    dt = 0

    while True:
        #check for window being closed by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill screen area in black
        screen.fill(000)
        pygame.display.flip()

        #limit framrate to 60fps
        dt = clock.tick(60)/1000
    
    
    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()