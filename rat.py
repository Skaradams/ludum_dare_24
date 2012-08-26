import os
import sys

from bloodyhell.world.actor import Actor

class Rat(Actor):

    def __init__(self, position, size):
        super(Rat, self).__init__(
            'sprite.rat', 'stance', position, size
        )
        self._walk_vel = 5.0
        self._jump_vel = 16.0

        self._run_multiple = 1
        self._x_vel = 0

        self.listen_key('right')
        self.listen_key('left')
        self.listen_key('space')

    def update(self):
        super(Rat, self).update()
        self.set_x_velocity(self._x_vel*self._run_multiple)

    def on_right_pressed(self):
        self._x_vel += self._walk_vel
        self.loop('walk')

    def on_right_released(self):
        self._x_vel -= self._walk_vel
        self.loop('stance')
    def on_left_pressed(self):
        self._x_vel -= self._walk_vel

    def on_left_released(self):
        self._x_vel += self._walk_vel

    def on_space_pressed(self):
        if self.get_y_velocity() == 0.0:
            self.set_y_velocity(self._jump_vel)

    def on_space_released(self):
        pass

    def on_collision(self, chunk, point):
        pass