from rat import Rat

class Lumi(Rat):
    def __init__(self, position, size, level):
        super(Lumi, self).__init__(position, size, level, 'lumi')