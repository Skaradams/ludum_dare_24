import os
import sys

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'bloodyhell')
))

from bloodyhell.world.actor import Actor

class Rat(Actor):

    def __init__(self, position, size):
        super(Rat, self).__init__(
            'platform.sprites.rat', 'stance', position, size
        )
        self.listen_key('right')
        self.listen_key('left')
        self.listen_key('space')

    def update(self):
        super(Rat, self).update()
  
    def on_collision(self, chunk, point):
        self._pasted = True