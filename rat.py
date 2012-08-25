import os
import sys

from bloodyhell.world.actor import Actor

class Rat(Actor):

    def __init__(self, position, size):
        super(Rat, self).__init__(
            'sprite.rat', 'stance', position, size
        )
        self._walk_vel = 3.0
        self._run_multiple = 1.5
        self._x_vel = 0

        self.listen_key('right')
        # self.listen_key('left')
        # self.listen_key('space')

    def update(self):
        super(Rat, self).update()
        self.set_x_velocity(self._x_vel)

    def on_right_pressed(self):
        self._x_vel += self._walk_vel
    
    def on_collision(self, chunk, point):
        pass