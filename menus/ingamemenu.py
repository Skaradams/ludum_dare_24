import os
import sys
import settings

from bloodyhell.view import View
from bloodyhell.view import Layer
from bloodyhell.widget import Widget
from bloodyhell.widget.interface import Interface
from bloodyhell.game import Game

from jukebox import JukeBox


class InGameMenu(View):

    CHOICES = ['resume', 'back', 'quit']

    def __init__(self):
        super(InGameMenu, self).__init__()
        self._interface = Interface('interfaces.ingamemenu')
        self.add_layer(self._interface, 100)
        self._choice = 0
        self._up_tap = False
        self._down_tap = False
        self.listen('quit')
        self.listen_key('up')
        self.listen_key('down')
        self.listen_key('return')

    def deselect_all(self):
        for choice in self.CHOICES:
            item = self._interface.get(choice)
            item.style('color', '#469638')

    def update_menu(self):
        self.deselect_all()
        item = self._interface.get(self.CHOICES[self._choice])
        item.style('color', '#becbcd')
        cursor = self._interface.get('cursor')
        top = 15 + self._choice * 20
        cursor.style('top', '%d%%' % top)

    def tap_down(self):
        self._choice += 1
        if self._choice >= len(self.CHOICES):
            self._choice = 0
        self.update_menu()

    def tap_up(self):
        self._choice -= 1
        if self._choice < 0:
            self._choice = len(self.CHOICES) - 1
        self.update_menu()

    def on_up_pressed(self):
        if not self._up_tap:
            self.tap_up()
            self._up_tap = True

    def on_up_released(self):
        self._up_tap = False

    def on_down_pressed(self):
        if not self._down_tap:
            self.tap_down()
            self._down_tap = True

    def on_down_released(self):
        self._down_tap = False

    def on_quit(self, event):
        JukeBox().stop()
        Game.quit()

    def back_to_title_menu(self):
        from menus.mainmenu import MainMenu
        self._navigator.set_current_view(MainMenu())

    def on_return_pressed(self):
        {
            'resume': self._navigator.pop,
            'back': self.back_to_title_menu,
            'quit': sys.exit
        }[self.CHOICES[self._choice]]()

    def on_return_released(self):
        pass
