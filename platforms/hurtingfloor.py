from bloodyhell.world.fence import Fence

class HurtingFloor(Fence):
    def __init__(self, data, image_id):

        super(HurtingFloor, self).__init__(
            (data['x'], data['y']),
            (data['width'], data['height']),
            image_id
        )

class SpadesDown(HurtingFloor):
    def __init__(self, data):
        super(SpadesDown, self).__init__(data, 'static.spades_bottom')
class SpadesUp(HurtingFloor):
    def __init__(self, data):
        super(SpadesUp, self).__init__(data, 'static.spades_top')
class SpadesLeft(HurtingFloor):
    def __init__(self, data):
        super(SpadesLeft, self).__init__(data, 'static.spades_left')
class SpadesRight(HurtingFloor):
    def __init__(self, data):
        super(SpadesRight, self).__init__(data, 'static.spades_right')