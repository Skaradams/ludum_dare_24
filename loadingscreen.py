import sys
import os
import settings
import threading
import Queue

from bloodyhell.view import View
from bloodyhell.layer import Layer
from bloodyhell.widget import Widget
from bloodyhell.widget.interface import Interface
from bloodyhell.layer.animatedlayer import AnimatedLayer

from menus.mainmenu import MainMenu


class LoadingTask(threading.Thread):

    def __init__(self, loader, queue):
        threading.Thread.__init__(self)
        self._loader = loader
        self._queue = queue

    def run(self):
        for package, sentence in settings.PACKAGES.items():
            self._queue.put(sentence)
            self._loader.load_package(package)
        self._queue.put(True)


class LoadingScreen(View):

    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.loader().load_package('loading')
        self.loader().load_package('interfaces')

        resolution = Widget.get_resolution()
        res_width, res_height = resolution
        self.add_layer(
            Layer(position=(0, 0), size=resolution).fill('191919'), 0
        )
        self._animation = AnimatedLayer(
            position=(res_width / 2 - 120, res_height / 2.3), size=(275, 50)
        )
        self._animation.set_animation('loading.tinyrat.walk')
        self.add_layer(self._animation, 1)
        self.listen('quit')
        self._interface = Interface('interfaces.loadingscreen')
        self.add_layer(self._interface, 100)
        self._queue = Queue.Queue()
        self._loading_task = LoadingTask(self.loader(), self._queue)
        self._loading_task.start()

    def on_frame(self, delta):
        super(LoadingScreen, self).on_frame(delta)
        message = None
        try:
            message = self._queue.get_nowait()
        except Queue.Empty:
            pass
        if message:
            if message == True:
                self._navigator.set_current_view(MainMenu())
            else:
                self._interface.get('message').attr('text', message)

    def on_quit(self, event):
        sys.exit()
