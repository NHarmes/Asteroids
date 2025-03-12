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
    
    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    #instantiate Player object and store it in a variable
    player = Player(x, y)
       

    while True:
        #check for window being closed by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill screen area in black
        screen.fill(000)

        #iterate over each item in the updatable group here
        #for each in updatable:
        #    each.update(dt)
        updatable.update(dt)

        #iterate over each item in the drawable group here
        for item in drawable:
            item.draw(screen)   

        pygame.display.flip()  
        #limit framrate to 60fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()