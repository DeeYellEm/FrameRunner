import random
from . import physicalobject, resources


class Ball(physicalobject.PhysicalObject):
    """A bouncing ball"""

    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(resources.ball_image, *args, **kwargs)

        #print('DLM: self.x: '+str(self.x)+' self.y: '+str(self.y))
        # Slowly rotate the ball as it moves
        self.rotate_speed = random.random() * 100.0 - 50.0
        if (random.random() < 0.5):
            self.rotate_speed = -1*self.rotate_speed
        # Assuming image is square-ish, so radius will just be half the width
        self.radius = self.image.width/2

    def update(self, dt):
        super(Ball, self).update(dt)
        self.rotation += self.rotate_speed * dt

    def handle_collision_with(self, other_object):
        super(Ball, self).handle_collision_with(other_object)
