import random
gameIsPlaying = ''
def ticTacToe():
    def drawBoard(board):
        print('------------')
        print('   |   |')
        print(' ' + board[7] + ' |' + board[8] + '  | ' + board[9])
        print('   |   |')
        print('----------')
        print('   |   |')
        print(' ' + board[4] + ' |' + board[5] + '  | ' + board[6])
        print('   |   |')
        print('----------')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def inputPlayerLetter():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
    def whoGoesFirst():
        if random.randint(0, 1) == 0:
            return 'player1'
        else:
            return 'computer'

    def playAgain():
        print('Do you want to play again?(yes or no)')
        return input().lower().startswith('y')

    def makeMove(board, letter, move):
        board[move] = letter
        
    def isWinner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9]== le) or
            (bo[4] == le and bo[5] == le and bo[6]== le) or
            (bo[1] == le and bo[2] == le and bo[3]== le) or
            (bo[7] == le and bo[4] == le and bo[1]== le) or
            (bo[8] == le and bo[5] == le and bo[2]== le) or
            (bo[9] == le and bo[7] == le and bo[3]== le) or
            (bo[7] == le and bo[5] == le and bo[3]== le) or
            (bo[9] == le and bo[5] == le and bo[1]== le))
    def getBoardCopy(board):
        dupeBoard = []
        for i in board:
            dupeBoard.append(i)
        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayerMove(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
            print('What player ones next move? (1-9)')
            move = input()
        return int(move)
    def chooseRandomMovefromList(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, computerLetter):
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'
        for i in range(1, 10): 
            copy = getBoardCopy(board) 
            if isSpaceFree(copy, i): 
                makeMove(copy, playerLetter, i) 
                if isWinner(copy, playerLetter): 
                    return i 

     
        move = chooseRandomMovefromList(board, [1, 3, 7, 9]) 
        if move != None: 
            return move 
     

        if isSpaceFree(board, 5): 
             return 5
    def isBoardFull(board): 
     # Return True if every space on the board has been taken. Otherwise return False. 
         for i in range(1, 10): 
             if isSpaceFree(board, i): 
                 return False 
         return True
    def computer():
        if isWinner(theBoard, playerLetter) and  choice == '1':
            drawBoard(theBoard)
            print('The computer has won.')
            gameIsPlaying = False
            bye = 1
            return bye


        else:
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('the game was a tie')
                tie = 1
                return tie
            
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)
        drawBoard(theBoard)
    print('welcome to tic tac toe')
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('the ' + turn + ' will go first')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                        
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('hooray! you have won the game')
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('the game was a tie')
                    break
                else:
                    turn = 'computer'
            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('the computer has beaten you! you lose.')
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('the game is a tie!')
                    break
                else:
                    turn = 'player'
        if not playAgain():
            break
def numberGuess():
    guessnumber = 0
    guess = 0

    number = random.randint(1,50)

    print('would you like to play a game? enter name here')
    name = input()
    print('well ' + name + ' guess the number im thinking of 1-50 or else,')
    while guessnumber < 10:
        print('guess!')
        guess = input()
        number = int(number)
        guess = int(guess)
        guessnumber = guessnumber+1

        if guess < number:
            print('to low bukaroo')

        if guess > number:
            print('to hot go low, bro')

        if guess == number:
            break

    guessnumber = str(guessnumber)
    name = str(name)
    if guess == number:
        guessnumber = str(guessnumber)
        
        print('yay ' + (name) + ' hast won in ' + (guessnumber) + ' guesses')

    if guess != number:
        number = str(number)
        print((name) + '... im disapointed, you lost poopy head. The numer was ' + (number))
def rockPaper():
    def rock():
        ai = random.randint(1,3)
        ai = str(ai)
        while choice == 'r' or choice == 'R':
            if ai == '1':
                print('it was a tie')
                ai = random.randint(1,3)
                ai = str(ai)
                redo = input()
                    
            elif ai == '2':
                print('You won! the AI choose Scissors')
                redo =1
                break
            elif ai == '3':
                print('you lost! the AI choose paper!')
                redo = 0
                return redo
        
            
    def Scissors():
        ai = random.randint(1,3)
        ai = str(ai)
        while choice == 's' or choice == 'S':
            if ai == '1':
                print('You lost! the ai used Rock')
               
                break
            elif ai == '2':
                print('it was a tie')
                ai = random.randint(1,3)
                ai = str(ai)
                redo = input()
            elif ai == '3':
                print('you won! the AI choose paper.')            
                break           
            break
        
    def paper():
        ai = random.randint(1,3)
        ai = str(ai)
        while choice == 'p' or choice == 'P':
            if ai == '1':
                print('You won! the AI choose rock')
                redo = 1
                break
            elif ai == '2':
                print('You lost! the AI choose Scissors')
                redo =1
                break
            elif ai == '3':
                
                while choice == 'r':
                    print('it was a tie')
                    ai = random.randint(1,3)
                    ai = str(ai)
                    redo = input()
    replay = 0
    while replay == 0 or replay == 'r':
        
        print('Pick Rock Paper or Scissors rock beats Scissors Scissors beat paper and paper   beats rock(you will be trying to beat an AI.)')
        choice = input()

        if choice == 'r' or choice == 'R':
            rock()
          
           
            
        if choice == 's' or choice == 'S':
            Scissors()
           
            
        if choice == 'p' or choice == 'P':
+            paper()
            
        print('do you want to play again?(r to play again p to quit)')
        replay = input()

def pickgame():
    game = random.randint(1,3)
    if game == 1:
        rockPaper()
    elif game == 2:
        numberGuess()
    else:
       ticTacToe()

                
