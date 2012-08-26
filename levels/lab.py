import os
import sys

from bloodyhell.level import Level
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from platforms.groundcage import *
from platforms.platformcage import *
from platforms.start import Start
from platforms.flag import Flag

from rat import Rat

class Lab(Level):
    
    def __init__(self, resolution, navigator):
        res_width, res_height = resolution
        super(Lab, self).__init__(camera_config={
            'target': (50, -21),
            'width': 20,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': 0.0, 'bottom': 10.0,
                       'right': 70.0, 'top': 50.0}
        }, gravity=(0, -33.0))
        self.listen('quit')
        # Load resources

        self._level = None
        self._start = None
        self._end = None
        self._next_level = None
        self._resolution = resolution
        self._navigator = navigator

        self._chunks = {
            'groundcage1': GroundCage1,
            'groundcage2': GroundCage2,
            'groundcage3': GroundCage3,
            'groundcage4': GroundCage4,
            'platformcage1': PlatformCage1,
            'platformcage2': PlatformCage2,
            'characterstart': Start,
            'end': Flag
        }        
                
        # Add background (filled with skyblue)
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('191919'),
            self.BACKGROUND
        )

    def on_quit(self, event):
        sys.exit()

    def add_chunks(self):
        for rect_id in self._level:
            datas = self._level[rect_id]
            try:
                chunk = self._chunks[rect_id.split('_')[0]](datas)

                if rect_id.split('_')[0] == "characterstart":
                    self._start = chunk

                if rect_id.split('_')[0] == "end":
                    self._end = chunk

                self.add_chunk(chunk, self.PLATFORM)
            except:
                pass
    
    def add_rat(self):
        print self._start.x
        rat_datas = self.loader().get_width_from_ratio('sprite.rat.stance_01', self._start.height())

        self._rat = Rat(position=(self._start.x(), self._start.y()), size=(rat_datas[0], rat_datas[1]))
        self._rat.set_hitbox({'left': 17.5})
        self.add_chunk(self._rat, self.SPRITES)
        self.world().camera().watch(self._rat, rat_datas[1]/3.5)

    def load_music(self):
        self.loader().play_sound('music.im_gonna_change')

    def on_frame(self, delta):
        super(Lab, self).on_frame(delta)
        print self
        if self._end.contains(self._rat) and self._next_level != None:
            print 'salut'
            self._navigator.set_current_view(self._next_level(self._resolution, self._navigator))

class Lab1(Lab):
    def __init__(self, resolution, navigator):
        super(Lab1, self).__init__(resolution, navigator)
        self._level = self.loader().get_raw_resource('svg_json.level_1')
        self._next_level = Lab2
        self.add_chunks()
        self.add_rat()
        # self.load_music()

class Lab2(Lab):
    def __init__(self, resolution, navigator):
        super(Lab2, self).__init__(resolution, navigator)
        self._level = self.loader().get_raw_resource('svg_json.level_2')
        self._next_level = None
        self.add_chunks()
        self.add_rat()
        # self.load_music()