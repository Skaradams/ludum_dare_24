import sys
import settings

sys.path.insert(0, settings.BLOODYHELL_DIR)

from bloodyhell.resourceloader import ResourceLoader
from bloodyhell.game import Game
from menus.mainmenu import MainMenu

RESOLUTION = (800, 600)
FPS = 25


def run():
    game = Game(
        'Ludum Dare 24',
        RESOLUTION,
        settings.RESOURCES_DIR,
        fps=FPS
    )

    loader = ResourceLoader()
    loader.load_package('static')
    loader.load_package('sprite')
    loader.load_package('svg_json')
    loader.load_package('music')

    navigator = game.navigator()
    navigator.set_current_view(MainMenu())
    game.run()

if __name__ == '__main__':
    run()
