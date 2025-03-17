import random

from circleshape import * 
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
     def __init__(self, x, y, radius):
          super().__init__(x, y, radius)

     #Override 'draw' method of circleshape
     def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

     #Override 'update' method of CircleShape
     def update(self, dt):
         self.position.x += (self.velocity.x * dt)
         self.position.y += (self.velocity.y * dt)

     #split mechanic
     def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
             return
         #define new radius
         new_radius = self.radius - ASTEROID_MIN_RADIUS
         
         #generate angle and create two new vectors in opposite offsets
         new_randangle = random.uniform(20, 50)
         new_veloc1 = self.velocity.rotate(new_randangle)
         new_veloc2 = self.velocity.rotate(-new_randangle)

         #increase velocities          
         new_veloc1 *= 1.2
         new_veloc2 *= 1.2
         
         #create new asteroid objects
         asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
         asteroid1.velocity = new_veloc1
         
         asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
         asteroid2.velocity = new_veloc2