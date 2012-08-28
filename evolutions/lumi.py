from rat import Rat
from bloodyhell.resourceloader import ResourceLoader

class Lumi(Rat):
    def __init__(self, position, level, base_height):
        size = ResourceLoader().get_width_from_ratio('lumi.stance_01', base_height)
        super(Lumi, self).__init__(
            position, level, 'lumi', size, track='now_i_can_see'
        )
