from bloodyhell.world.fence import Fence

class PlatformCage(Fence):
    def __init__(self, index, data):

        super(PlatformCage, self).__init__(
            (data['x'], data['y']),
            (data['width'], data['height']),
            'static.platform_cage_' + str(index)
        )

class PlatformCage1(PlatformCage):
    def __init__(self, data):
        super(PlatformCage1, self).__init__(1, data)

class PlatformCage2(PlatformCage):
    def __init__(self, data):
        super(PlatformCage2, self).__init__(2, data)

class PlatformCage3(PlatformCage):
    def __init__(self, data):
        super(PlatformCage3, self).__init__(3, data)

class PlatformCage4(PlatformCage):
    def __init__(self, data):
        super(PlatformCage4, self).__init__(4, data)