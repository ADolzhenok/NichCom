from voice_assistant.get_audio import get_audio_rus
from voice_assistant.speak import speak_rus

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(' 1 | 2 | 3')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |  ')
    print('-----------')
    print(' 4 | 5 | 6')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' 7 | 8 | 9')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) \
           or (bo[4] == le and bo[5] == le and bo[6] == le) \
           or (bo[1] == le and bo[2] == le and bo[3] == le) \
           or (bo[1] == le and bo[4] == le and bo[7] == le) \
           or (bo[2] == le and bo[5] == le and bo[8] == le) \
           or (bo[3] == le and bo[6] == le and bo[9] == le) \
           or (bo[1] == le and bo[5] == le and bo[9] == le) \
           or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        speak_rus('Пожалуйста, выберите позицию для икса из интервала от одного до девяти')
        move = get_audio_rus()
        for char in move:
            if char == 'один':
                move = 1
            if char.isdigit():
                move = char
                break
        try:
            if move == 'один':
                move = 1
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    speak_rus('Извините, но это место занято!')
            else:
                speak_rus('Пожалуйста, скажите число из списка!')
        except:
            print('Пожалуйста, назовите число!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    speak_rus('Добро пожаловать в крестики-нолики! Взгляните на экран')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            speak_rus('К сожаления, O одержал победу!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                speak_rus('Ничья!')
            else:
                insertLetter('O', move)
                speak_rus(f'Компьютер поставил O на позицию {move}')
                printBoard(board)
        else:
            speak_rus('X победил в этой игре! Хорошая работа!')
            break

    if isBoardFull(board):
        speak_rus('Спасибо за игру')


def tic_tac_toe_rus():
    while True:
        speak_rus('Хотите сыграть?')
        answer = get_audio_rus()
        if answer == 'да':
            global board
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
        else:
            break

