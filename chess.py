CAPTURE = 1
BLOCKED = 2
OPEN = 3

class Piece:
    def __init__(self):
        pass

    def check_square(self, x, y):
        square = self._board[y][x]
        if square is not None:
            if square.color != self.color:
                return CAPTURE
            return BLOCKED
        return OPEN

 
class Rook(Piece):
    def __init__(self, board):
       self._board = board 
    
    def get_available_moves(self):
        x = self.x
        while x > board.width:
            x -= 1
            x_and_y = (x, self.y)
            state = self.check_square(**x_and_y)
            if state in (CAPTURE, OPEN):
                yield x_and_y
            if state in (BLOCKED, CAPTURE):
                break
                
class Board:

    def __init__(self):
        self._board = [[None] * 8] * 8        

    def render(self):
        for row in self._board:
            for square in row:
                if square:
                    print(square.symbol, end='')
                else:  
                    print('*', end='')
            print('') 

if __name__ == "__main__":
    r = Rook()
    board = Board()
    board.render()
