from rat import Rat

class GrassHopper(Rat):
    def __init__(self, position, size, level):
        super(GrassHopper, self).__init__(
            position, size, level, 'rat', 'music.i_need_to_get_higher'
        )
        self._jump_vel = 30.0
