import os
import sys

from bloodyhell.level import Level
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from platforms.groundcage import *
from rat import Rat


class Level1(Level):

    def __init__(self, resolution):
        res_width, res_height = resolution
        super(Level1, self).__init__(camera_config={
            'target': (502.7735, -2132.4165000000003),
            'width': 2000,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': 0.0, 'bottom': 0.0,
                       'right': 70.0, 'top': 10.0}
        }, gravity=(0, -9.8))
        self.listen('quit')
        # Load resources

        level = self.loader().get_raw_resource('svg_json.level_1')


        self._chunks = {
            'groundcage1': GroundCage1,
            'groundcage2': GroundCage2,
            'groundcage3': GroundCage3,
            'groundcage4': GroundCage4
        }
        chunk = None
        for rect_id in level:
            datas = level[rect_id]
            class_id = rect_id.split('_')[0]
            try:
                chunk = self._chunks[rect_id.split('_')[0]](datas)
                self.add_chunk(chunk)
            except:
                pass
                

        # Add background (filled with skyblue)
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('87CEEB'),
            self.BACKGROUND
        )

        # Create Actor 
        # rat = Rat(position=(1.5, 4.0), size=(0.5, 1.0))
        # self.add_chunk(rat, self.SPRITES)

        # Lock camera to Rat
        

        #self.loader().play_sound('platform.music.samba')

        # self.add_layer(Interface('interface.xml'), 100)

    def on_quit(self, event):
        sys.exit()

