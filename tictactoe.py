# Tic-tac-toe

import random


def draw_board(board):
    # Displays the playing field, the cells of which will be filled.

    # Board is a list of 10 lines for drawing the playing field (0 is ignored)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    # Allowing the player to enter the letter he chooses.
    # Returns a list in which the player's letter is the first element
    # and the computer's letter is the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you choose X or O?')
        letter = input().upper()

    # Player's letter is the 1st element and the computer's letter is the 2nd.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Random selection of the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    # Returns True if player won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # through the mid
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # through the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the center
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal 1
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal 2


def get_boardcopy(board):
    # Copy of the playing field.
    boardcopy = []
    for i in board:
        boardcopy.append(i)
    return boardcopy


def is_space_free(board, move):
    # Returns True if a move to a free cell has been made.
    return board[move] == ' '


def get_player_move(board):
    # Allowing the player to make a move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Your next move? (1-9)')
        move = input()
    return int(move)


def choose_random_move_fromlist(board, moves_list):
    # Returns a valid move, given the lists of moves made and of filled cells.
    # Returns None if there are no more valid moves
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Taking into account the filling of the playing field and the letter of the
    # computer, determines the valid move and returns it.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Algorithm for the "Tic-Tac-Toe" AI:
    # First we check whether we will win by making the next move.
    for i in range(1, 10):
        boardcopy = get_boardcopy(board)
        if is_space_free(boardcopy, i):
            make_move(boardcopy, computer_letter, i)
            if is_winner(boardcopy, computer_letter):
                return i

    # Check whether the player wins by making the next move, and block it
    for i in range(1, 10):
        boardcopy = get_boardcopy(board)
        if is_space_free(boardcopy, i):
            make_move(boardcopy, player_letter, i)
            if is_winner(boardcopy, player_letter):
                return i

    # We try to occupy one of the corners, if there are any available
    move = choose_random_move_fromlist(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # We try to occupy the mid if it's available
    if is_space_free(board, 5):
        return 5

    # Meke a move on one side
    return choose_random_move_fromlist(board, [2, 4, 6, 8])


def is_board_full(board):
    # Returns True if a cell on the playing field is occupied, otherwise False
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Tic-Tac-Toe')

while True:
    # Reloading the playing field
    theboard = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('' + turn + ' goes first.')
    game_is_playing = True
    while game_is_playing:

        if turn == 'Player':
            # Player's move
            draw_board(theboard)
            move = get_player_move(theboard)
            make_move(theboard, player_letter, move)

            if is_winner(theboard, player_letter):
                draw_board(theboard)
                print('Hurray! You have won!')
                game_is_playing = False
            else:
                if is_board_full(theboard):
                    draw_board(theboard)
                    print('A draw')
                    break
                else:
                    turn = 'Computer'

        else:
            # Computer's move
            move = get_computer_move(theboard, computer_letter)
            make_move(theboard, computer_letter, move)

            if is_winner(theboard, computer_letter):
                draw_board(theboard)
                print("The computer won! You've lost.")
                game_is_playing = False
            else:
                if is_board_full(theboard):
                    draw_board(theboard)
                    print('A draw')
                    break
                else:
                    turn = 'Player'

    print('Shall we play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
