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
        self.set_hitbox({'left': 4.0, 'top': 2.0})
class SpadesUp(HurtingFloor):
    def __init__(self, data):
        super(SpadesUp, self).__init__(data, 'static.spades_top')
        self.set_hitbox({'left': 4.0, 'top': 2.0})
class SpadesLeft(HurtingFloor):
    def __init__(self, data):
        super(SpadesLeft, self).__init__(data, 'static.spades_left')
        self.set_hitbox({'left': 2.0, 'top': 4.0})
class SpadesRight(HurtingFloor):
    def __init__(self, data):
        super(SpadesRight, self).__init__(data, 'static.spades_right')
        self.set_hitbox({'left': 2.0, 'top': 4.0})