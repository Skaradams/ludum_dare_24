from bloodyhell.world.fence import Fence

class InvisibleWall(Fence):
    def __init__(self, data):

        super(InvisibleWall, self).__init__(
            (data['x'], data['y']),
            (data['width'], data['height']),
            'static.blank'
        )
