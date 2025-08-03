class Aircraft:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self):
        self.height += self.speed

# And say we want to also model more specific kinds of aircraft. We could create a more specific Helicopter class like this:
class Helicopter:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed
        self.direction = 0

    def fly_up(self):
        self.height += self.speed

    def rotate(self):
        self.direction += 90

# By adding Aircraft in parentheses after Helicopter, we're saying "make Helicopter a child class of Aircraft". 
# Now Helicopter inherits all the properties and methods of Aircraft!

class Helicopter(Aircraft):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self):
        self.direction += 90

# So the Helicopter's constructor says "first, call the Aircraft constructor, 
# and then additionally set the direction property".
# Now, say we want to create a Jet class. Again, because all jets are aircraft, 
# we can inherit from Aircraft again.
class Jet(Aircraft):
    def __init__(self, speed):
        # Jets always start on the ground
        super().__init__(0, speed)

    def go_supersonic(self):
        self.speed *= 2