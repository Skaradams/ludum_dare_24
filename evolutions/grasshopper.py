from rat import Rat

class GrassHopper(Rat):
    def __init__(self, position, size, level):
        super(GrassHopper, self).__init__(position, size, level, 'grasshopper')
        self._jump_vel = 30.0