import os
import sys

from bloodyhell.world.fence import Fence
from bloodyhell.resourceloader import ResourceLoader

class GroundCage(Fence):
    def __init__(self, index, data):

        super(GroundCage, self).__init__(
            (data['x'], data['y']),
            (data['width'], data['height']),
            'static.ground_cage_' + str(index)
        )

class GroundCage1(GroundCage):
    def __init__(self, data):
        super(GroundCage1, self).__init__(1, data)

class GroundCage2(GroundCage):
    def __init__(self, data):
        super(GroundCage2, self).__init__(2, data) 

class GroundCage3(GroundCage):
    def __init__(self, data):
        super(GroundCage3, self).__init__(3, data) 

class GroundCage4(GroundCage):
    def __init__(self, data):
        super(GroundCage4, self).__init__(4, data) 
