import os
import sys

from bloodyhell.level import Level
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from platforms.groundcage import *
from platforms.platformcage import *
from platforms.hurtingfloor import *

from platforms.start import Start
from platforms.flag import Flag

from pill import *
from rat import Rat
from evolutions.grasshopper import GrassHopper

class Lab(Level):
    
    def __init__(self, resolution, navigator):
        res_width, res_height = resolution
        super(Lab, self).__init__(camera_config={
            'target': (50, -21),
            'width': 25,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': 0.0, 'bottom': -30.0,
                       'right': 70.0, 'top': 50.0}
        }, gravity=(0, -33.0))
        self.listen('quit')

        self._level = None
        self._start = None
        self._end = None
        self._hurting_floors = []
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
            'platformcage3': PlatformCage3,
            'platformcage4': PlatformCage4,
            'characterstart': Start,
            'end': Flag,
            'spades': Spades,
            'pillevolutionb': GrassHopperPill
        }        
                
        # Add background (filled with grey)
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('191919'),
            self.BACKGROUND
        )

    def on_quit(self, event):
        sys.exit()

    def add_chunks(self):
        print "ADDING CHUNKS FOR : " + self.__class__.__name__
        for rect_id in self._level:
            data = self._level[rect_id]
            self.add_platform(rect_id.split('_')[0], data)
    
    def add_platform(self, chunk_id, data):
        if chunk_id in self._chunks:
            print chunk_id
            chunk = self._chunks[chunk_id](data)
            if chunk_id == "characterstart":
                self._start = chunk

            if chunk_id == "end":
                self._end = chunk

            if chunk_id == "spades":
                self._hurting_floors.append(chunk)
            super(Lab, self).add_chunk(chunk, self.BACKGROUND)

    def add_rat(self):
        rat_datas = self.loader().get_width_from_ratio('rat.stance_01', self._start.height())

        self._rat = Rat(position=(self._start.x(), self._start.y()), size=(rat_datas[0], rat_datas[1]), level=self)
        self._rat.set_hitbox({'left': 17.5, 'top': 3.0})
        self.add_chunk(self._rat, self.SPRITES)
        self.world().camera().watch(self._rat, rat_datas[1]/3.5)
        # self.world().camera().watch(self._rat, -rat_datas[1]*1.5)

    @classmethod
    def reset(cls, resolution, navigator):
        print navigator
        navigator.set_current_view(cls(resolution, navigator))

    def navigator(self):
        return self._navigator

    def resolution(self):
        return self._resolution

    def load_music(self):
        self.loader().play_sound('music.im_gonna_change')

    def on_frame(self, delta):
        super(Lab, self).on_frame(delta)
        if self._rat.contains(self._end) and self._next_level != None:
            self._navigator.set_current_view(self._next_level(self._resolution, self._navigator))

class Lab1(Lab):
    def __init__(self, resolution, navigator):
        print "I AM LEVEL 1"
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