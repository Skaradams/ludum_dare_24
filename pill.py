from bloodyhell.world.decoration import Decoration

class Pill(Decoration):
    pill_instances = {
        'grasshopper': [],
        'tinyrat': [],
        'lumi': [],
    }
    def __init__(self, data, image_id):
        self._x = data['x']
        self._y = data['y']
        self._width = data['width']
        self._height = data['height']
        super(Pill, self).__init__((self._x, self._y), (self._width, self._height), image_id)  

    @staticmethod
    def clear_instances():
        Pill.pill_instances = {
            'grasshopper': [],
            'tinyrat': [],
            'lumi': [],
        }
        
class GrassHopperPill(Pill):
    def __init__(self, data):
        super(GrassHopperPill, self).__init__(data, 'pill_grasshopper')
        self.layer().set_animation('pill_grasshopper.pill_grasshopper')
        Pill.pill_instances['grasshopper'].append(self)

class TinyRatPill(Pill):
    def __init__(self, data):
        super(TinyRatPill, self).__init__(data, 'pill_tinyrat')
        self.layer().set_animation('pill_tinyrat.pill_tinyrat')
        Pill.pill_instances['tinyrat'].append(self)

class LumiPill(Pill):
    def __init__(self, data):
        super(LumiPill, self).__init__(data, 'pill_lumi')
        self.layer().set_animation('pill_lumi.pill_lumi')
        Pill.pill_instances['lumi'].append(self)
