from BOARD.game_board import *


class game_interface:

    def printBars(self):
        line = '---'
        for i in range(80):
            line = line + '---'
        print(line)

    def GameInstructions(self):
        self.printBars()
        print('Game instructions')
        print('Players take turns in writing their symbol in a cell.\n The restriction is that you can only play \n in a cell if all its neighbours are empty')
        print('When you make a move it will be marked with an X \n and all of your neighbors will be marked \n with a *.In case of an error, an message will')
        print('printed on the screen')
        print('You will move first,after the computer will move and so on')
        print('HAPPY GAME SESSION, DEAR USER!')

        self.printBars()

    def showGameCommands(self):

        print('play - to start a game')
        print('settings - to modify board size')
        print('help - some informations about the game')
        print('x - for exit')

    def settingsOptions(self):
        self.printBars()

        print('The board is set by default to a 10*10 size')
        print('If you want to modify the size enter an integer')
        print('between 6 and 25')

        self.printBars()


    def getCommand(self):
        '''
        Here we take a command from the user.
        The command will be returned and used
        in the function that called this fct.
        '''
        command = input('Enter your command: ')
        return command

    def getHumanMove(self):
        '''
        The human will introduce as a move
        something like : number and Char
        This function gets the command from the user
        and transforms it into coordinates for the
        board
        '''

        x = input('Enter line number: ')
        y = input('Enter column: ')

        if len(x) == 0 or len(y) == 0:
            raise ValueError('Line/Column cannot be empty')
        alphaLet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        alphaLet = alphaLet.split(' ')
        for let in str(x):
            if let not in '0123456789':
                raise ValueError('Line should be an integer')
        if y.upper() not in alphaLet:
            raise ValueError('Column should be an upper case letter from the board!')

        cooridinates = []
        cooridinates.append(int(x))
        index = 0

        while index < len(alphaLet):
            if y.upper() == alphaLet[index]:
                cooridinates.append(index)
                return cooridinates
            index += 1

        return cooridinates

    def game_exe(self,supportBoard):
         '''
         In this function will take place the
         game. Any kind of exception that might
         apppear will be handeled in this function.
         '''
         while True:
            try:
                coordinatesHumanMove = self.getHumanMove()
                supportBoard._makeMove(coordinatesHumanMove,'x')

                print(supportBoard)

                #we check if the human player made the last possible move
                if supportBoard.availableCells() == 0:
                    return 'GAME WON :D'

                #now the computer should make the move

                supportBoard.computerMove(coordinatesHumanMove)
                if supportBoard.availableCells() == 0:
                    return  'NICE TRY,BUT YOU LOSE :('
                print('COMPUTER MOVEMENT:')
                print(supportBoard)
            except ValueError as er:
                print(er)



    def mainMenu(self):

        size = 10

        while True:

                self.showGameCommands()
                command = self.getCommand()

                if command.lower() == 'x':
                    return 0
                elif command.lower() == 'help':
                    self.GameInstructions()
                elif command.lower() == 'settings':
                     self.settingsOptions()
                     try:
                         n = int(input('Enter number >'))
                         if n < 6 or n > 25:
                             print("Size does not match requirements.No changes have been made!")
                         else:
                             size = n
                     except ValueError:
                         print('ENTER A DIGIT BETWEEN 6 AND 25')
                elif command.lower() == 'play':
                     supportBoard = gameBoard(size)
                     print('Creating game board ...')
                     print('This is the board.')
                     print(supportBoard)
                     print('Start game')
                     message = self.game_exe(supportBoard)
                     print(message)
                else:
                    print('Invalid Command!')




gamePlay = game_interface()

gamePlay.mainMenu()




