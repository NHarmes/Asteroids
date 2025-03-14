from circleshape import * 
from constants import SHOT_RADIUS

class Shot(CircleShape):
     def __init__(self, x, y):
          super().__init__(x, y, SHOT_RADIUS)

     #Override 'draw' method of circleshape
     def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, width=2)

     #Override 'update' method of CircleShape
     def update(self, dt):
         self.position.x += (self.velocity.x * dt)
         self.position.y += (self.velocity.y * dt)