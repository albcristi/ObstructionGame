
from BOARD.Texttable import Texttable
from random import choice

class gameBoard:
    '''
    This class will represent the board in which
    the game will take place
    '''

    def __init__(self,size):

        if self.checkStringNumber(str(size)) == 0:
            raise ValueError('Size has to be an integer between 1 and 25')
        if size > 25 or size < 5:
            raise ValueError('Size can not be more than 25 and less than 0!')
        self.__size = int(size)
        self.__data = []
        for i in range(size):
            self.__data.append([' ']*self.__size)

    @property
    def size(self):
        return self.__size

    def checkStringNumber(self,string):
        '''
        Here we test if a string can be transformed
        into a number
        INPUT:
          string- which is bassicly a string
        OUTPUT:
         0 or 1 - 0 for false and 1 for true
        '''

        for ch in string:
            if ch not in '0123456789':
                return 0

        return 1

    def __str__(self):
        '''
        Here we build the string reprezentation
        of the table
        '''

        t  = Texttable()
        '''
        Build row header
        '''
        res = [' ','A']
        i = self.size-1
        while i>0:
            res.append(chr(ord(res[-1])+1))
            i -= 1
        t.header(res)
        for i in range(self.size):
            res = []
            for j in range(self.size):
                res.append(self.__data[i][j])

            t.add_row([i]+res)

        return t.draw()

    def _getBoardLimits(self):
        '''
        This function will return list of length
        2, representing the upper bounds of the
        board (column, line)
        '''
        limits = []
        #
        # alphaLett =  'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        # alphaLett = alphaLett.split(' ')
        #
        # limits.append(alphaLett[self.size-1])
        limits.append(self.size-1)
        limits.append(self.size-1)
        return limits

    def _checkCellState(self,coordinates):
        '''
        In this function we check the state of a given
        cell.
        The values for a cell can be:
            ' ' if the cell is free
             x  if the cell is marked by
             the human player
             0 if the cell is marked by
             the computer
             * if the cell is in the vecinity
             of a 1 or a 2
        '''

        return self.__data[coordinates[0]][coordinates[1]]

    def _getNeighbors(self,coordinates):
        '''
        Here we return a list that returns the
        neighbors of a cell from the board-
        point given by its coordinates -
        '''

        x = coordinates[0]
        y = coordinates[1]

        neigh = [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]

        '''
        We elimanate all the neighbors that are not inside the board
        '''
        index = 0
        while index < len(neigh):
            if neigh[index][0] < 0 or neigh[index][0] > self.size - 1:
                neigh.pop(index)
            elif neigh[index][1] < 0 or neigh[index][1] > self.size - 1:
                neigh.pop(index)
            else:
                index += 1

        return neigh


    def _markNeighbors(self,coordinates):
        '''
        For a given cell,we mark all of it's
        free neighboors with *
        '''
        neigh = self._getNeighbors(coordinates)

        for cell in neigh:
            if self._checkCellState(cell) == ' ':
                self.__data[cell[0]][cell[1]] = '::'

    def _moveValidator(self,coordinates):
        '''
        INPUT: COORDINATES -a tuple containing
        the coordinates of a point on the board

        In this function we validate an move,
        meaning that:
           o we check if the coordinates do fit in
         the board
           o we check if the place where we want to
        place the next move is free
        '''
        boardLimits = self._getBoardLimits()

        er = []

        if coordinates[0] > boardLimits[0]:
            er.append('Line value exceeds the maximum size')

        if coordinates[1] > boardLimits[1]:
            er.append('Column value exceeds the maximum size')

        if len(er)!= 0:
            raise  ValueError(er)
        if self._checkCellState(coordinates) != ' ':
            er.append('INVALID MOVE.CELL IS ALREADY USED')
        if len(er) > 0:
            raise ValueError(er)

    def _makeMove(self,coordinates,playerMove):
        '''
        Here we make a move on the board
        Firstly we make sure that the given
        coordindates are valid, after we make
        sure that the cell given by the coord.
        is free and after that we mark the cell
        by the value of playerMove(X-for human,0-
        for computer) and we also mark the neigh.
        of the given cell with *
        '''

        self._moveValidator(coordinates)

        if self._checkCellState(coordinates) != ' ':
             er = []
             er.append('Make sure that the cell you want to mark is free \n A free cell is not marked by any kind symbols!')
             raise ValueError(er)
        self.__data[coordinates[0]][coordinates[1]] = playerMove
        self._markNeighbors(coordinates)

    def availableCells(self):
        '''
        We return 1 if there are free cells and 0
        otherwise
        '''

        for i in range(self.size):
            for j in range(self.size):
                if self._checkCellState([i,j]) == ' ':
                    return 1

        return 0

    def gameStatus(self):
        '''
        This function will check after each move
        if the next round is possible.
        If there are no other cells free, it means
        that the game reached its end
        The function return 0 if there are no more
        av. moves and 1 otherwise
        '''
        return self.availableCells()


    '''
     IN THIS PART WILL BE SOME FUNCTIONS THAT WILL BE USED BY THE COMPUTER TO MAKE ITS MOVES
    '''
    def emptyCells(self):
        '''
        This function returns a list with all the
        empty cells from the board.Based on this
        cells,the computer will make its move
        against the human player.
        '''
        if self.availableCells() == 0:
            return []

        emptyCells =  []

        for i in range(self.size):
            for j in range(self.size):
                if self.__data[i][j] == ' ':
                    emptyCells.append([i,j])

        return emptyCells

    def unmarkedNeigh(self,coordinates):
        '''
        For a give point from the table,
        we return all of its free neighboors
        '''

        neigh = self._getNeighbors(coordinates)
        freeNeigh =  []

        for n in neigh:
            if self.__data[n[0]][n[1]] == ' ':
                freeNeigh.append(neigh)

        return freeNeigh
    def maxMove(self):
        '''
        In this case, we return the coordinates
        of where the player could make a move in
        such a way that it will make a move that
        covers the maximum number of neighbors at
        that time
        '''

        possibleMoves = self.emptyCells()

        winner = possibleMoves[0]

        for cell in possibleMoves:
            if len(self.unmarkedNeigh(winner)) < len(self.unmarkedNeigh(cell)):
                winner = cell

        return winner

    def minimalMove(self):
        '''
        Just like maxMove, but it returns the move
        that will mark the minimum number of neighbors
        at that time of the game
        '''

        possibleMoves = self.emptyCells()

        winner = possibleMoves[0]

        for cell in possibleMoves:
            if len(self.unmarkedNeigh(winner)) > len(self.unmarkedNeigh(cell)):
                winner = cell

        return winner

    def computerMove(self,humanMove):
        '''
        This function will do the move of the
        computer on the board.
        Functions that help to decide what
        kind of move the computer should do
        are minmalMove and maxMove.
        The computer will try to change it's
        type of movements, from movements
        that will cover a large area to moves
        that will also cover small areas.
        '''

        #if len(self.emptyCells()) > self.size*self.size - 15:
        '''
        It means that there's a large free area for making 
        moves, in this way the computer will try to cover
        a large area from the booard
        '''
        if self._checkCellState([humanMove[1],humanMove[0]]) == ' ':
            self._makeMove([humanMove[1],humanMove[0]],'0')
        elif len(self.emptyCells()) > len(self.emptyCells())//2:
             self._makeMove(self.maxMove(),'0')
             return 0
        else:
            self._makeMove(self.minimalMove(), '0')
            return 0
        # elif  len(self.emptyCells()) > self.size*3:
        #     ch = choice([1,2])
        #     if ch == 1:
        #         self._makeMove(self.maxMove(), '0')
        #     else:
        #         self._makeMove(self.minimalMove(),'0')
        #     return 0
        # else:
        #     self._makeMove(self.minimalMove(), '0')

