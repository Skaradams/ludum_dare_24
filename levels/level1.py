import os
import sys

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'bloodyhell')
))

from bloodyhell.level import Level
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from rat import Rat


class Level1(Level):

    def __init__(self, resolution):
        res_width, res_height = resolution
        super(Level1, self).__init__(camera_config={
            'target': (5.0, 3.5),
            'width': 15.0,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': 0.0, 'bottom': 0.0,
                       'right': 70.0, 'top': 10.0}
        }, gravity=(0, -9.8))
        self.listen('quit')
        # Load resources

        # Add background (filled with skyblue)
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('87CEEB'),
            self.BACKGROUND
        )

        # Create Actor 
        rat = Rat(position=(1.5, 4.0), size=(0.5, 1.0))
        self.add_chunk(rat, self.SPRITES)

        # Lock camera to Rat
        self.world().camera().watch(rat)

        #self.loader().play_sound('platform.music.samba')

        # self.add_layer(Interface('interface.xml'), 100)

    def on_quit(self, event):
        sys.exit()

