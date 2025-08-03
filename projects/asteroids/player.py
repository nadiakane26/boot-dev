
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

# Player inherits from CircleShape to represent the player's ship in the game.
class Player(CircleShape):
  def __init__(self, x, y):
    # Calls the parent class's constructor
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.shoot_timer = 0

  # in the player class
  # A player will look like a triangle, even though we'll use a circle to represent its hitbox
  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
    
    # Drawer the player overriding the draw method from CircleShape.
  def draw(self, screen):
    points = self.triangle()
    # The screen object
    # A color (use "white")
    # A list of points (use self.triangle() that we provided for you)
    # A line width (use 2)
    pygame.draw.polygon(screen, "white", points, 2)

  def rotate(self, dt):
    # Rotate the player by PLAYER_TURN_SPEED degrees per second
    self.rotation += PLAYER_TURN_SPEED * dt
    # Normalize the rotation to be between 0 and 360 degrees
    self.rotation %= 360
  
  def update(self, dt):
    if self.shoot_timer > 0:
        self.shoot_timer -= dt

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        # Rotate left
        self.rotate(-dt)
    if keys[pygame.K_d]:
        # Rotate right
        self.rotate(dt)
    if keys[pygame.K_w]:
        # Move forward
        self.move(dt)
    if keys[pygame.K_s]:
        # Move backward
        self.move(-dt)
    if keys[pygame.K_SPACE]:
        # Shoot a shot
        self.shoot()
  
  def move(self, dt):
     # We start with a unit vector pointing straight up from (0, 0) to (0, 1).
     # We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
     forward = pygame.Vector2(0, 1).rotate(self.rotation)
     # We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
     # Add the vector to our position to move the player.
     self.position += forward * PLAYER_SPEED * dt
  
  def shoot (self):
    # Create a new shot at the player's position
    shot = Shot(self.position.x, self.position.y)
    # Set the shot's velocity to be in the direction the player is facing
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    shot.velocity = forward * PLAYER_SHOOT_SPEED
    return shot