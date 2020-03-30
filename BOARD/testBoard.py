

from BOARD.game_board import *
from unittest import TestCase


class TestBoard(TestCase):
    '''
    In this class we will test some of the features that
    the game board should have.
    '''

    def setUp(self):
        return TestCase.setUp(self)

    def tearDown(self):
        return  TestCase.tearDown(self)


    def test(self):
        '''
        In this function we'll test multiple of
        the board features
        '''

        testBoard = gameBoard(10)

        '''
        Here we test to see if the board that we wanted 
        to create really has the size 10*10
        '''
        assert testBoard.size == 10


        '''
        This is how our board should look like:
        +---+---+---+---+---+---+---+---+---+---+---+
        |   | A | B | C | D | E | F | G | H | I | J |
        +===+===+===+===+===+===+===+===+===+===+===+
        | 0 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 1 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 2 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 3 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 4 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 5 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 6 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 7 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 8 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        | 9 |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+

        '''

        '''
        Here we test if the limits that the function
        _getBoardLimits returns  [9,9]
        we can deduce that J is the 10-th element from 
        the list of the upper case alph. letters
        
        '''

        limits = testBoard._getBoardLimits()

        assert limits[0] == 9
        assert limits[1] == 9

        '''
        We try to create a board that exceeds the maximum
        allowed size for a board.
        '''

        try:
            wrongBoard = gameBoard(28)
            assert False
        except:
            pass

        '''
        We try to create a board with size that is a string 
        '''

        try:
            wrongBoard = gameBoard('alala')
            assert False
        except:
            pass

        '''
        We try to create a board that has as size 
        a string that contains both digits and chars.
        '''

        try:
            wrongBoard = gameBoard('0124315gg234132')
            assert False
        except:
            pass

        '''
        We try to create a string that has a negative number
        as size,which should be impossible
        '''

        try:
            wrongBoard = gameBoard(-12)
            assert False
        except:
            pass

        semiPlayBoard = gameBoard(10)

        assert semiPlayBoard._checkCellState([0,1]) == ' '
        '''
        Only in an upper layer, one of the coordinates will
        be enetered as a letter(in the game  UI),here the 
        coordinares are numbers
        '''
        semiPlayBoard._makeMove([0,9],1)
        '''
        Here we make sure that when we make 
        a move, the available neigh. are marked
        with *
        '''
        assert semiPlayBoard._checkCellState([0,8]) == '*'
        '''
        We try an invalid move
        '''
        try:
            semiPlayBoard._makeMove([0,8],'x')
            assert False
        except:
            pass
        '''
        Here we test if the function that returns the neigh. of 
        a cell works as it should for the general case and the 
        bound cases when we don't have all the 8 possible neigh.
        '''
        '''
        For [0,0] we should have :
        [[1, 0], [0, 1], [1, 1]]
        '''
        neigh = semiPlayBoard._getNeighbors([0,0])
        assert neigh == [[1, 0], [0, 1], [1, 1]]

        '''
        For [2,4]:
        [[1, 3], [2, 3], [3, 3], [1, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
        '''
        neigh = semiPlayBoard._getNeighbors([2,4])

        assert neigh == [[1, 3], [2, 3], [3, 3], [1, 4], [3, 4], [1, 5], [2, 5], [3, 5]]

        '''
        For [9,8]:
        [[8, 7], [9, 7], [8, 8], [8, 9], [9, 9]]
        '''
        neigh = semiPlayBoard._getNeighbors([9,8])
        assert  neigh == [[8, 7], [9, 7], [8, 8], [8, 9], [9, 9]]

        '''
        We put some moves and chek the function check cells
        '''

        for i in range(0,10,4):
            semiPlayBoard._makeMove([i,i],'x')

        assert semiPlayBoard.availableCells() == 1
        #print(semiPlayBoard.emptyCells())
        print(semiPlayBoard)
        print(semiPlayBoard.maxMove())
        print(semiPlayBoard.minimalMove())

