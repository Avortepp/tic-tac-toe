import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Выберите 'X' или 'O':")
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'people'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # По верху
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # По центру
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # По низу
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # По левой стороне
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # По центру
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # По правой стороне
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # По диагонали
            (bo[9] == le and bo[5] == le and bo[1] == le))    # По диагонали

def getBoardCopy(board):
    return board[:]

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    availableMoves = [move for move in movesList if isSpaceFree(board, move)]
    if availableMoves:
        return random.choice(availableMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'O':
        playerLetter = 'X'
    else:
        playerLetter = 'X'

    # Проверка, победим ли мы, сделав следующий ход.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Проверка, победит ли игрок, сделав следующий ход.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Выбор случайного хода
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    return all(not isSpaceFree(board, i) for i in range(1, 10))

print('Игра "Крестики-нолики"')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' ходит первым')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'people':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Ничья!")
                    break
                else:
                    turn = 'computer'
        else:
            # Ход компьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер выиграл!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Ничья!")
                    break
                else:
                    turn = 'people'

    print("Хотите сыграть еще? да или нет?")
    play_again = input().lower()
    if not play_again.startswith('д'):
        break
