import os
import sys

from bloodyhell.level import Level
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from platforms.groundcage import *
from platforms.platformcage import *
from platforms.invisiblewall import InvisibleWall
from platforms.hurtingfloor import *

from platforms.start import Start
from platforms.flag import Flag

from shadow import *
from backlayers import *
from menus.ingamemenu import InGameMenu
from comicstrip import ComicStrip

from pill import *
from rat import Rat
from evolutions.grasshopper import GrassHopper
from evolutions.tinyrat import TinyRat
from evolutions.lumi import Lumi

class Lab(Level):
    rats = {
        'rat': None,
        'grasshopper': None,
        'tinyrat': None,
        'lumi': None,
    }
    def __init__(self, resolution, navigator, strip_id='static.comic_strip_1'):
        res_width, res_height = resolution
        super(Lab, self).__init__(camera_config={
            'target': (50, -21),
            'width': 30,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': -1000, 'bottom': -1000,
                       'right': 1000, 'top': 1000}
        }, gravity=(0, -33.0))
        self.listen('quit')

        self._strip_id = strip_id
        self._level = None
        self._start = None
        self._end = None
        self._hurting_floors = []
        self._next_level = None
        self._resolution = resolution
        self._navigator = navigator
        self._frame_limit = 1
        self._frame_count = 0

        self._chunks = {
            'groundcage1': GroundCage1,
            'groundcage2': GroundCage2,
            'groundcage3': GroundCage3,
            'groundcage4': GroundCage4,
            'platformcage1': PlatformCage1,
            'platformcage2': PlatformCage2,
            'platformcage3': PlatformCage3,
            'platformcage4': PlatformCage4,
            'backlayer1': BackLayer1,
            'backlayer2': BackLayer2,
            'backlayer3': BackLayer3,
            'backlayer4': BackLayer4,
            'blank': InvisibleWall,
            'characterstart': Start,
            'end': Flag,
            'shadows': Shadow,
            'spadesup': SpadesUp,
            'spadesleft': SpadesLeft,
            'spadesright': SpadesRight,
            'spadesdown': SpadesDown,
            'pillevolutiona': TinyRatPill,
            'pillevolutionb': GrassHopperPill,
            'pillevolutiond': LumiPill
        }
        Pill.clear_instances()
        Shadow.clear_instances()
        self._shadow_layer = Layer(position=(0, 0), size=resolution).fill('000000')

        # Add background (filled with grey)
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('191919'),
            self.BACKGROUND
        )
        self.listen_key('escape')

    def on_quit(self, event):
        self._navigator.push(InGameMenu())

    def add_chunks(self):
        for rect_id in self._level:
            data = self._level[rect_id]
            self.add_platform(rect_id.split('_')[0], data)

    def add_platform(self, chunk_id, data):
        if chunk_id in self._chunks:
            # Position Hack (gap between platforms)

            chunk = self._chunks[chunk_id](data)
            if chunk_id == "characterstart":
                self._start = chunk

            if chunk_id == "end":
                self._end = chunk

            if chunk_id == "spades":
                self._hurting_floors.append(chunk)

            if isinstance(chunk, BackLayer):
                layer_pos = self.BACKGROUND

            else:
                layer_pos = self.BACKGROUND_1
            super(Lab, self).add_chunk(chunk, layer_pos)

    def add_rat(self):
        self._rat = Lab.rats['normal']
        self.reset_rats()
        # self._rat.set_hitbox({'left': 17.5, 'top': 3.0})
        self.add_chunk(self._rat, self.SPRITES)
        self._rat.set_position((self._start.x(), self._start.y()))
        self.watch_rat()
        # self.world().camera().watch(self._rat, -rat_datas[1]*1.5)
        self._rat.play_track()

    def reset_rats(self):
        Lab.rats['normal'].reset(self)
        Lab.rats['grasshopper'].reset(self)
        Lab.rats['tinyrat'].reset(self)
        Lab.rats['lumi'].reset(self)

    @classmethod
    def reset(cls, resolution, navigator):
        navigator.set_current_view(cls(resolution, navigator))

    def navigator(self):
        return self._navigator

    def resolution(self):
        return self._resolution

    def load_music(self):
        self.loader().play_sound('music.im_gonna_change')

    def on_frame(self, delta):
        super(Lab, self).on_frame(delta)
        if self._rat.contains(self._end): 
            if self._next_level != None:
                self._navigator.set_current_view(self._next_level(self._resolution, self._navigator))
                self._navigator.set_current_view(ComicStrip(self._next_level(self._resolution, self._navigator), self._strip_id))
            else:
                self._navigator.set_current_view(ComicStrip(None, self._strip_id))

        if self._frame_count == self._frame_limit:
            self.pill_spawn()
            self.check_shadows()
            self._frame_count = 0
        self._frame_count += 1

    def change_rat(self, new_rat):
        self.reset_rats()
        self.remove_chunk(self._rat)
        self._rat = new_rat
        self.add_chunk(self._rat, self.SPRITES)
        self.watch_rat()
        self._rat.play_track()

    def pill_spawn(self):
        for pill in Pill.pill_instances['grasshopper']:
            if self._rat.contains(pill) and self._rat.__class__ != GrassHopper:
                print "rat contains pill"
                new_rat = Lab.rats['grasshopper']
                new_rat.set_position(self._rat.position())
                # new_rat = GrassHopper(position=(self._rat.position()[0], self._rat.position()[1]), level=self, base_height=self._start.height())
                self.change_rat(new_rat)

        for pill in Pill.pill_instances['tinyrat']:
            if self._rat.contains(pill) and self._rat.__class__ != TinyRat:
                new_rat = Lab.rats['tinyrat']
                new_rat.set_position(self._rat.position())
                # new_rat = TinyRat(position=(self._rat.position()[0], self._rat.position()[1]), level=self, base_height=self._start.height())
                self.change_rat(new_rat)

        for pill in Pill.pill_instances['lumi']:
            if self._rat.contains(pill) and self._rat.__class__ != Lumi:
                new_rat = Lab.rats['lumi']
                new_rat.set_position(self._rat.position())
                self.change_rat(new_rat)

    def check_shadows(self):
        applyshadow = False
        for shadow in Shadow.shadow_instances:
            if shadow.contains(self._rat) and self._rat.__class__ != Lumi:
                applyshadow = True

        if applyshadow:
            self.add_layer(
                self._shadow_layer,
                self.NEAR_DECORATION
            )
        else:
            self.remove_layer(self._shadow_layer)

    def watch_rat(self):
        rat_width, rat_height = self._rat.real_size()
        rat_x, rat_y = self._rat.position()
        self.world().camera().watch(self._rat)
        if self._rat.__class__ == TinyRat:
            self.world().camera().set_width(rat_width * 9)
        else:
            self.world().camera().set_width(rat_width * 5)
        self.world().camera().set_y_high_filter_threshold(rat_height * 8)

    def on_escape_pressed(self):
        self._navigator.push(InGameMenu())

    def on_escape_released(self):
        pass

class Lab1(Lab):
    def __init__(self, resolution, navigator):
        super(Lab1, self).__init__(resolution, navigator, 'static.comic_strip_2')

        self._level = self.loader().get_raw_resource('svg_json.level_1')
        self._next_level = Lab2
        self.add_chunks()

        Lab.rats['normal'] = Rat(position=(self._start.x(), self._start.y()), level=self, base_height=self._start.height())
        Lab.rats['grasshopper'] = GrassHopper(position=(self._start.x(), self._start.y()), level=self, base_height=self._start.height())
        Lab.rats['tinyrat'] = TinyRat(position=(self._start.x(), self._start.y()), level=self, base_height=self._start.height())
        Lab.rats['lumi'] = Lumi(position=(self._start.x(), self._start.y()), level=self, base_height=self._start.height())

        self.add_rat()

        # self.load_music()

class Lab2(Lab):
    def __init__(self, resolution, navigator):
        super(Lab2, self).__init__(resolution, navigator, 'static.comic_strip_3')

        self._level = self.loader().get_raw_resource('svg_json.level_2')
        self._next_level = Lab3
        self.add_chunks()
        self.add_rat()
        # self.load_music()

class Lab3(Lab):
    def __init__(self, resolution, navigator):
        super(Lab3, self).__init__(resolution, navigator, 'static.comic_strip_4')

        self._level = self.loader().get_raw_resource('svg_json.level_3')
        self._next_level = Lab4
        self.add_chunks()
        self.add_rat()

class Lab4(Lab):
    def __init__(self, resolution, navigator):
        super(Lab4, self).__init__(resolution, navigator, 'static.comic_strip_5')

        self._level = self.loader().get_raw_resource('svg_json.level_4')
        self._next_level = Lab5
        self.add_chunks()
        self.add_rat()

class Lab5(Lab):
    def __init__(self, resolution, navigator):
        super(Lab5, self).__init__(resolution, navigator, 'static.comic_strip_6')
        self._level = self.loader().get_raw_resource('svg_json.level_5')
        self._next_level = None
        self.add_chunks()
        self.add_rat()
