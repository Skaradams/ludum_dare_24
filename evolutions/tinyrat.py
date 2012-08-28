from rat import Rat
from bloodyhell.resourceloader import ResourceLoader

class TinyRat(Rat):
    def __init__(self, position, level, base_height):
        size = ResourceLoader().get_width_from_ratio('tinyrat.stance_01', base_height)
        divider = 17
        (width, height) = (size[0]/divider, size[1]/divider)
        size = (width, height)
        super(TinyRat, self).__init__(
            position, level, 'tinyrat', size,  track='music.that_tiny_me', hitbox={'left': 20.0, 'top': 5.0}
        )
        self._walk_vel = 5.0
        self._jump_vel = 15.0

