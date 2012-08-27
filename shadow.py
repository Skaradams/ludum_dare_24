from bloodyhell.world.decoration import Decoration

class Shadow(Decoration):
    shadow_instances = []
    def __init__(self, data):
        self._x = data['x']
        self._y = data['y']
        self._width = data['width']
        self._height = data['height']
        super(Shadow, self).__init__((self._x, self._y), (self._width, self._height), "static.blank")
        Shadow.shadow_instances.append(self)

    @classmethod
    def clear_instances(self):
        Shadow.shadow_instances = []
