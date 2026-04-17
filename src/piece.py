class Piece:
    def _init_(self, name, color, value, texture, teture_rect=None):
        pass

class Pawn(Piece):
    def _init_(self, color):
        if color == 'white':
            self.dir=-1