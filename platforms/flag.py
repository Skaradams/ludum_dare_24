from bloodyhell.world.decoration import Decoration

class Flag(Decoration):
    def __init__(self, data):
        self._x = data['x']
        self._y = data['y']
        self._width = data['width']
        self._height = data['height']
        super(Flag, self).__init__((self._x, self._y), (self._width, self._height), 'static.flag')

    def x(self):
        return self._x

    def y(self):
        return self._y

    def width(self):
        return self._width

    def height(self):
        return self._height