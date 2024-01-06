from voice_assistant.get_audio import get_audio_eng
from voice_assistant.speak import speak_eng

board = [' ' for x in range(10)]

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(color.BOLD + '   |   |  ' + color.END)
    print(color.BOLD + ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + color.END)
    print(color.BOLD + '   |   |  ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   |  ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |' + color.END)


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        speak_eng(color.BOLD + 'Please select a position to place an \'X\' (1-9)' + color.END)
        move = get_audio_eng()
        for char in move:
            if char.isdigit():
                move = char
                break
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    speak_eng('Sorry, this space is occupied!')
            else:
                speak_eng('Please type a number within the range!')
        except:
            print('Please type a number!')


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
    speak_eng(color.BOLD + 'Welcome to Tic Tac Toe! Look at the screen' )
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            speak_eng('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                speak_eng('Tie Game!')
            else:
                insertLetter('O', move)
                speak_eng(color.BOLD + f'Computer placed an \'O\' in position {move}' + color.END)
                printBoard(board)
        else:
            speak_eng(color.BOLD + 'X\'s won this time! Good Job!' + color.END)
            break

    if isBoardFull(board):
        print('Tie Game!')


def tic_tac_toe_eng():
    while True:
        speak_eng('Do you want to play again?')
        answer = get_audio_eng()
        if answer == 'yes':
            global board
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
        else:
            break

