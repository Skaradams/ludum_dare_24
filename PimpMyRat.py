import settings

from bloodyhell.game import Game
from loadingscreen import LoadingScreen


def run():
    game = Game(
        'Pimp My Rat',
        settings.RESOLUTION,
        settings.RESOURCES_DIR,
        fps=settings.FPS
    )
    navigator = game.navigator()
    navigator.set_current_view(LoadingScreen())
    game.run()

if __name__ == '__main__':
    run()
