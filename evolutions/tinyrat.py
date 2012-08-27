from rat import Rat

class TinyRat(Rat):
    def __init__(self, position, size, level):
        super(TinyRat, self).__init__(
            position, size, level, 'tinyrat', 'music.that_tiny_me'
        )
