import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'bloodyhell')
))

from bloodyhell.resourceloader import ResourceLoader
from bloodyhell.game import Game
from levels.lab import *

RESOLUTION = (800, 600)
FPS = 25

def run():
    game = Game(
        'Ludum Dare 24',
        RESOLUTION,
        os.path.join(os.path.dirname(__file__), 'res'),
        fps=FPS
    )

    loader = ResourceLoader()
    loader.load_package('static')
    loader.load_package('sprite')
    loader.load_package('svg_json')
    loader.load_package('music')

    navigator = game.navigator()
    navigator.set_current_view(Lab2(RESOLUTION, navigator))
    game.run()

if __name__ == '__main__':
    run()
