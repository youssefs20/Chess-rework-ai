
class Move :

    def __init__(self, initial, final):
        # squares are represented as tuples (x,y) where x and y are integers between 0 and 7
        self.initial = initial
        self.final= final