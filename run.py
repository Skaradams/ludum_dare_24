import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'bloodyhell')
))


from bloodyhell.game import Game
from levels.level1 import Level1

from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from bloodyhell.world.actor import Actor
from bloodyhell.world.fence import Fence
from bloodyhell.widget.interface import Interface


RESOLUTION = (800, 600)
FPS = 25

def run():
    game = Game(
        'Ludum Dare 24',
        RESOLUTION,
        os.path.join(os.path.dirname(__file__), 'res'),
        fps=FPS
    )
    print os.path.abspath(os.path.join(os.path.dirname(__file__), 'res'))
    game.navigator().set_current_view(Level1(RESOLUTION))
    game.run()

if __name__ == '__main__':
    run()
