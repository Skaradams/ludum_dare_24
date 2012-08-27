from rat import Rat
from bloodyhell.resourceloader import ResourceLoader

class GrassHopper(Rat):

    def __init__(self, position, level, base_height):
        size = ResourceLoader().get_width_from_ratio('grasshopper.stance_01', base_height)
        super(GrassHopper, self).__init__(
            position, level, 'grasshopper', size, track='music.i_need_to_get_higher'
        )
        self._jump_vel = 30.0
        self._walk_vel = 4.0
        

