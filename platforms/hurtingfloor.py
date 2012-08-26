from bloodyhell.world.fence import Fence

class HurtingFloor(Fence):
    def __init__(self, data, image_id):

        super(HurtingFloor, self).__init__(
            (data['x'], data['y']),
            (data['width'], data['height']),
            image_id
        )

class Spades(HurtingFloor):
    def __init__(self, data):
        super(Spades, self).__init__(data, 'static.flag')