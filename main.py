# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #instantiate Player object and store it in a variable
    player = Player(x, y)
    asteroidfield = AsteroidField()   
    

    while True:
        #check for window being closed by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for rock in asteroids:
            #check for collisions with player
            if rock.collides(player) == True:
                print("GameOver!")
                sys.exit(0)

            #check for collisions with asteroids
            for shot in shots:
                if rock.collides(shot) == True:
                    rock.split()
                    shot.kill()

        #fill screen area in black
        screen.fill(000)     

        #iterate over each item in the drawable group here
        for item in drawable:
            item.draw(screen)   

        pygame.display.flip()  
        #limit framrate to 60fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()