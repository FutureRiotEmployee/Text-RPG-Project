import random
import time
gameIsPlaying = ''

name = 'derk'
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
            return 'player'
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
            (bo[9] == le and bo[7] == le and bo[8]== le) or
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
                makeMove(copy, computerLetter, i) 
                if isWinner(copy, computerLetter): 
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
        if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print('The master has won.')
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
                    win = True
                    return win
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
                    print('the master has beaten you! you lose.')
                    drawBoard(theBoard)
                    
                    gameIsPlaying = False
                elif isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('the game is a tie!')
                    break
                else:
                    turn = 'player'
def numberGuess():
    guessnumber = 0
    guess = 0

    number = random.randint(1,50)

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
        win = True
        return win
    if guess != number:
        number = str(number)
        print((name) + '... Im disapointed, you lost. The numer was ' + (number))
        
def rockPaper():

    def rock():
        ai = random.randint(1,3)
        ai = str(ai)
        while choice == 'r' or choice == 'R':
            if ai == '1':
                print('it was a tie')
                ai = random.randint(1,3)
                ai = str(ai)
                redo = 0
                return redo
                    
            if ai == '2':
                print('You won! the master choose Scissors')
                win = True
                return win
                win = True
                
            else:
                print('you lost! the master choose paper!')
                win = False
        
            
    def Scissors():
        ai = random.randint(1,3)
        ai = str(ai)
        while choice == 's' or choice == 'S':
            if ai == '1':
                print('You lost! the master used Rock')
                break
            elif ai == '2':
                print('it was a tie')
                ai = random.randint(1,3)
                ai = str(ai)
                redo = 0
                return redo
            elif ai == '3':
                print('you won! the master choose paper.')
                win = True
                return win
                break           
            break
        
    def paper():
        ai = random.randint(1,3)
        ai = str(ai)
        while choice == 'p' or choice == 'P':
            if ai == '1':
                print('You won! the master choose rock')
                win = True
                return win
                break
            
            elif ai == '2':
                print('You lost! the master choose Scissors')
                
                break
            
            elif ai == '3':                
                while choice == 'r':
                    print('it was a tie')
                    ai = random.randint(1,3)
                    ai = str(ai)
                    redo = 0
                    return redo
                            
    win = False
def pickgame():
    game = random.randint(1,3)
    if game == 1:
        win = rockPaper()
    elif game == 2:
        win = numberGuess()
    elif game == 3 :
        win = ticTacToe()
    else:
        win = False
    return win
def intro():
    print('after traveling far and wide you have found him')
    #time.sleep(2.5)
    print('the game master')
    print('you walk into his cave and he says "I have been waiting for this')
    #time.sleep(1)
    print('waiting for a challenger')
    #time.sleep(1.5)
    print('I will play 3 random games 5 times')
    print('you will have to beat me all 5 times to take my title')
    print('the games are rock paper scissors, guees a number and tic tac toe')
    print('this will be easy you say')
    #time.sleep(1)
    print('lets see, he responds')
    
def levels():
    win1 = pickgame()
    if win1 == True:
        print('you have beat level 1')
        win1 = pickgame()
        if win1 = True:
            print('you have beat level 2')
            #time.sleep(1)
            win1 = pickgame()
                if win1:
                    print('getting closer, you have beat level 3')
                    print('you palms are sweaty you think of your moms spaghetti')
                    #time.sleep(1)
                    win1 = pickgame()
                    if win1
                        print('I am so close you think')
                        print('just 2 more wins')
                        #time.sleep(1)
                        print('the master says nothing')
                        #time.sleep(.5)
                        win1 = pickgame()
                        if win1:
                            print('you say nothing')
                            #time.sleep(1)
                            win1 = pickgame()
                            if win1:
                                print('this is the final round are you sure you want to continue? he asks')
                                print('yes')
                                print('ok then lets go')
                                win1 = pickgame()
                                if win1:
                                    print('i did it! you exclaim')
                                    print('but then the master starts laughing')
                                    #time.sleep(3)
                                    print('you think you won?')
                                    print('you never did')
                                    #time.sleep(1)
                                    print('before you got another word out of your mouth he jumps up and stabs you')
                                    print('the last thing you see is him laughing standing on you dying body...')
                                    #time.sleep(1)
    while replay != 'y' or != 'n':
        print('would you like to play again? (y or n)')
        replay = input()
    return replay
intro()
again = pickgame
while again = 'y':
    again = pickgame
                                  
                        
                        
                    
        
        


                
                                  
                        
                        
                    
        
        
