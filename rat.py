import os
import sys

from bloodyhell.world.actor import Actor

class Rat(Actor):

    def __init__(self, position, size):
        super(Rat, self).__init__(
            'static.sprites.rat', 'stance', position, size
        )
        self.listen_key('right')
        self.listen_key('left')
        self.listen_key('space')

    def update(self):
        super(Rat, self).update()
  
    def on_collision(self, chunk, point):
        self._pasted = True
