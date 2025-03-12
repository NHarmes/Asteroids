from circleshape import * 

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