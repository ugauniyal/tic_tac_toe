import shutil
import random
import os
from terminaltables import AsciiTable, SingleTable

board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

continue_game = 'Y'

player = 'X'


winner = None
game_in_progress = True


# Board of Game
def show_board():
    data = []
    data.append([board[0], board[1], board[2]])
    data.append([board[3], board[4], board[5]])
    data.append([board[6], board[7], board[8]])
    table_result = SingleTable(data)
    table_result.inner_row_border = True
    print(table_result.table)
    print('\n')

# Handling the first turn


def first_turn():
    print('\n')
    player1 = input('Enter your name ')
    player2 = input('Enter your name ')
    players = [player1, player2]
    print('\n')
    print(random.choice(players) + ' will play first.')
    print('\n')

# Play Game


def play_game():
    valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    global continue_game
    global board
    global game_in_progress
    while game_in_progress and win_check(player) == None and tie_check() == None:
        position_input = int(
            input('Enter the position of your choice (1-9): '))
        print('\n')

        if position_input not in valid_inputs:
            print('The position is invalid. Please enter between 1 and 9')
            continue

        pos = position_input - 1
        if board[pos] != '_':
            print('The position is already filled, choose other position')
            print('\n')
            continue

        board[pos] = player
        show_board()
        win_check(player)
        print('\n')
        turn_swap()


# Swap the turns between the players
def turn_swap():
    global player
    player = 'X' if player != 'X' else 'O'

# Check if someone won


def win_check(player):
    global board
    global winner
    global game_in_progress

    win_situation = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for wins in win_situation:
        if all(board[pos] == player for pos in wins):
            game_in_progress = False
            winner = player
            print(winner, 'is the winner')
            return True

    return None


# Check if the game is tied
def tie_check():
    global game_in_progress
    global continue_game
    if "_" not in board:
        print('Game Tie')
        return True
    else:
        return None

# Asking if Player wants to play again


def ask_continue_game():
    global board
    global continue_game
    global game_in_progress
    global player

    print('\n')
    print('Do you want to play again? To play again type "Y" or press any other key to suspend.')
    continue_game = input()
    print('\n')

    while continue_game == 'Y':

        game_in_progress = True
        board = ['_', '_', '_',
                 '_', '_', '_',
                 '_', '_', '_']
        player = 'X'
        play_game()
        ask_continue_game()

    else:
        return False


columns = shutil.get_terminal_size().columns
print("TIC-TAC-TOE".center(columns))


print('\n')
show_board()
first_turn()
play_game()
ask_continue_game()
