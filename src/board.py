from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares: list[list[Square | None]] = \
            [[None] * COLS for row in range(ROWS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')


    # def calc_moves(self, piece, row, col):
    #     # Calculate possible moves for a piece at a given position
    #     moves = []
    #     if piece.name == 'pawn':
    #         direction = -1 if piece.color == 'white' else 1
    #         start_row = 6 if piece.color == 'white' else 1

    #         # Move forward
    #         if self.is_empty(row + direction, col):
    #             moves.append((row + direction, col))

    #             # Move two squares from starting position
    #             if row == start_row and self.is_empty(row + 2 * direction, col):
    #                 moves.append((row + 2 * direction, col))

    #         # Capture diagonally
    #         for dc in [-1, 1]:
    #             if self.is_enemy(row + direction, col + dc, piece.color):
    #                 moves.append((row + direction, col + dc))

    #     # Implement move logic for other pieces (rook, knight, bishop, queen, king)
    #     # ...

    #     return moves
    def calc_moves(self, piece, row, col):


        def knight_moves():
            # 8 possible moves for a knight
            possible_moves = [
                (row - 2, col - 1), (row - 2, col + 1),
                (row - 1, col - 2), (row - 1, col + 2),
                (row + 1, col - 2), (row + 1, col + 2),
                (row + 2, col - 1), (row + 2, col + 1)

            ]
            # 
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isEmptyOrRival(piece.color):
                        
                        # creating squares of a new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a movwe  
                        move = Move(initial, final)
                        #append 
                        piece.add_move(move)
        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            pass

        elif isinstance(piece, Rook):
            pass
        
        elif isinstance(piece, Queen):
            pass

        elif isinstance(piece, King):
            pass

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        if color == 'white':
            row_pawn, row_other = (6,7)
        else:
            row_pawn, row_other = (1,0)
        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        self.squares[row_other][4] = Square(row_other, 4, King(color))