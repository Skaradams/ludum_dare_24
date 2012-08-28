import os
import sys
import settings

from bloodyhell.view import View
from bloodyhell.view import Layer
from bloodyhell.widget.interface import Interface
from bloodyhell.widget import Widget
from menus.mainmenu import MainMenu

class EndGame(View):
    def __init__(self):
        super(EndGame, self).__init__()
        self.add_layer(
            Layer(position=(0, 0), size=Widget.get_resolution()).fill('191919'),
            0
        )
        self._interface = Interface('interfaces.endgame')
        self.add_layer(self._interface, 100)
        self.listen_key('return')

    def on_return_pressed(self):
        self._navigator.set_current_view(MainMenu())

    def on_return_released(self):
        pass