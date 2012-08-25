import os
import sys

from bloodyhell.level import Level
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from platforms.groundcage import *
from platforms.platformcage import *
from rat import Rat

class Level1(Level):
    
    def __init__(self, resolution):
        res_width, res_height = resolution
        super(Level1, self).__init__(camera_config={
            'target': (50, -21),
            'width': 20,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': 0.0, 'bottom': 10.0,
                       'right': 70.0, 'top': 50.0}
        }, gravity=(0, -33.0))
        self.listen('quit')
        # Load resources

        level = self.loader().get_raw_resource('svg_json.level_1')

        self._chunks = {
            'groundcage1': GroundCage1,
            'groundcage2': GroundCage2,
            'groundcage3': GroundCage3,
            'groundcage4': GroundCage4,
            'platformcage1': PlatformCage1,
            'platformcage2': PlatformCage2
        }

        chunk = None
        for rect_id in level:
            datas = level[rect_id]
            class_id = rect_id.split('_')[0]
            try:
                chunk = self._chunks[rect_id.split('_')[0]](datas)
                self.add_chunk(chunk, self.PLATFORM)
            except:
                pass
                
        # Add background (filled with skyblue)
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('060202'),
            self.BACKGROUND
        )

        # Create Actor 
        rat_datas = self.loader().get_width_from_ratio('sprite.rat.stance_01', level['characterstart']['height'])
        print "RAT SIZE : ", rat_datas
        rat = Rat(position=(level['characterstart']['x'], level['characterstart']['y']), size=(rat_datas[0], rat_datas[1]))
        rat.set_hitbox({'left': 17.5})
        self.add_chunk(rat, self.SPRITES)

        # Lock camera to Rat
        self.world().camera().watch(rat, rat_datas[1]/3.5)

        self.loader().play_sound('music.im_gonna_change')

        # self.add_layer(Interface('interface.xml'), 100)

    def on_quit(self, event):
        sys.exit()

