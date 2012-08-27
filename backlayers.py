from bloodyhell.world.decoration import Decoration

class BackLayer(Decoration):
    def __init__(self, data, image_id):
        self._x = data['x']
        self._y = data['y']
        self._width = data['width']
        self._height = data['height']
        super(BackLayer, self).__init__((self._x, self._y), (self._width, self._height), 'static.'+image_id)  

class BackLayer1(BackLayer):
    def __init__(self, data):
        super(BackLayer1, self).__init__(data, 'backlayer1')

class BackLayer2(BackLayer):
    def __init__(self, data):
        super(BackLayer2, self).__init__(data, 'backlayer2')

class BackLayer3(BackLayer):
    def __init__(self, data):
        super(BackLayer3, self).__init__(data, 'backlayer3')

class BackLayer4(BackLayer):
    def __init__(self, data):
        super(BackLayer4, self).__init__(data, 'backlayer4')