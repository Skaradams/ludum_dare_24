import os
import sys
import settings

from bloodyhell.view import View
from bloodyhell.view import Layer
from bloodyhell.widget.interface import Interface
from bloodyhell.widget import Widget

class ComicStrip(View):
    def __init__(self, level, image_id):
        super(ComicStrip, self).__init__()

        self.add_layer(
            Layer(position=(0, 0), size=Widget.get_resolution()).fill('ffffff'),
            0
        )

        (res_width,res_height) = Widget.get_resolution()
        self._res_width = res_width
        self._res_height = res_height
        self._level = level
        self._interface = Interface(
            os.path.join(settings.INTERFACES_DIR, 'comicstrip.xml')
        )
        self._height = self.loader().get_raw_resource(image_id).get_height()
        self._increment = 100

        self._interface.get('comicstrip').style('background-image', image_id)
        self.add_layer(self._interface, 100)

        self.listen_key('return')
        self.listen_key('down')
        self.listen_key('up')

    def on_down_pressed(self):
        top = int(self._interface.get('comicstrip').style('top'))
        
        print self._res_height - int(self._interface.get('comicstrip').style('top')), self._height
        if self._res_height - int(self._interface.get('comicstrip').style('top')) <= self._height:
            self._interface.get('comicstrip').style('top', str(top-self._increment))

    def on_down_released(self):
        pass

    def on_up_pressed(self):
        top = int(self._interface.get('comicstrip').style('top'))
        
        if int(self._interface.get('comicstrip').style('top')) < 0:
            self._interface.get('comicstrip').style('top', str(top+self._increment))

    def on_up_released(self):
        pass

    def on_return_pressed(self):
        print self._res_height - int(self._interface.get('comicstrip').style('top')), self._height
        if self._res_height - int(self._interface.get('comicstrip').style('top')) > self._height:
            self._navigator.set_current_view(self._level)

    def on_return_released(self):
        pass