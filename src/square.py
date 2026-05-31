class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece 
    

    def has_piece(self):
        return self.piece is not None
    

    def isEmptyOrRival(self, color):
        return self.has_piece() or self.hasRivalPiece(color)
    
    def hasRivalPiece(self,color):
        return self.has_piece() and self.piece.color != color 
    
    def isEmpty(self):
        return not self.has_piece()
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    
    #static method is going to be used in the board class to check if a move is within the board limits
    # we can use it in the game class to check if a move is valid before making it
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7 :
                return False
        return True