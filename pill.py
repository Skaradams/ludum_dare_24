from bloodyhell.world.decoration import Decoration

class Pill(Decoration):
    def __init__(self, data, image_id):
        self._x = data['x']
        self._y = data['y']
        self._width = data['width']
        self._height = data['height']
        super(Pill, self).__init__((self._x, self._y), (self._width, self._height), image_id)

class GrassHopperPill(Pill):
    def __init__(self, data):
        super(GrassHopperPill, self).__init__(data, 'static.pill_grasshopper')
