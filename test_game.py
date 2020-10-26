import pytest
from tictactoe import TicTacToe


def test_init():
    game1 = TicTacToe()
    game1.update_board(3)
    game1.__init__()
    assert game1.get_board() == [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

    game2 = TicTacToe()
    game2.swap_player()
    game2.__init__()
    assert game2.get_player() == 'O'

    game3 = TicTacToe()
    game3.__init__()
    assert game3.get_winner() == None

    game3 = TicTacToe()
    win_possibility = [1,2,3,4,5,6,7]
    for pos in win_possibility:
        game3.update_board(pos)
        game3.swap_player()
    game3.__init__()
    assert game3.get_winner() == None

    game4 = TicTacToe()
    game4.__init__()
    assert game4.get_player_names() == []

    game4 = TicTacToe()
    game4.set_player_names('Tony Stark', 'Peter Parker') 
    game4.__init__()
    assert game4.get_player_names() == []

def test_set_game_state():
    game1 = TicTacToe()
    game1.set_game_state(True)
    assert game1.is_running() == True
    game1.set_game_state(False)
    assert game1.is_running() == False


def test_set_get_player_names():
    game1 = TicTacToe()
    player_names = ['Tony Stark', 'Peter Parker']
    game1.set_player_names(player_names[0], player_names[1])
    assert game1.get_player_names().sort() == player_names.sort()


def test_get_current_player_name():
    game1 = TicTacToe()
    player_names = ['Tony Stark', 'Peter Parker']
    game1.set_player_names(player_names[0], player_names[1])
    assert game1.get_current_player_name() in player_names

def test_update_board():
    game1 = TicTacToe()
    assert game1.update_board(20) == False

    game2 = TicTacToe()
    assert game2.update_board(3)
    assert game2.board[2] == game2.player
    assert game2.update_board(3) == False
    assert game2.board[2] == game2.player

def test_get_player():
    game1 = TicTacToe()
    assert game1.get_player() == 'O'
    game1.swap_player()
    assert game1.get_player() == 'X'

def swap_player():
    game1 = TicTacToe()
    assert game1.get_player() == 'O'
    game1.swap_player()
    assert game1.get_player() == 'X'
    game1.swap_player()
    assert game1.get_player() == 'O'

def test_check_win():
    game1 = TicTacToe()
    win_possibility = [1,2,3,4,5,6]
    for pos in win_possibility:
        game1.update_board(pos)
        game1.swap_player()
        assert game1.check_win() == False
    game1.update_board(7)
    assert game1.check_win() == True

def test_get_winner():
    game1 = TicTacToe()
    win_possibility = [1,2,3,4,5,6,7,8]
    for pos in win_possibility:
        game1.update_board(pos)
        game1.swap_player()
    assert game1.check_win() == True
    assert game1.get_winner() == 'O'

    game2 = TicTacToe()
    win_possibility = [2,1,3,5,4,9,6]
    for pos in win_possibility:
        game2.update_board(pos)
        game2.swap_player()

    assert game2.check_win() == True
    assert game2.get_winner() == 'X'

    game3 = TicTacToe()
    game3.update_board(1)
    game3.update_board(4)
    assert game3.check_win() == False
    assert game3.get_winner() == None
    game3.__init__()
    assert game3.check_win() == False
    assert game3.get_winner() == None

    game4 = TicTacToe()
    tie_possibilities = [1,2,3,6,4,7,5,8,9]
    for pos in tie_possibilities:
        game4.update_board(pos)
        game4.swap_player()
    assert game4.check_win() == False
    assert game4.get_winner() == None



def test_check_tie():
    game1 = TicTacToe()
    game1.update_board(1)
    game1.update_board(3)
    game1.update_board(7)
    assert game1.check_tie() == False
    game1.__init__()
    assert game1.check_tie() == False

    game2 = TicTacToe()
    tie_possibilities = [1,2,3,6,4,7,5,8,9]
    for pos in tie_possibilities:
        game2.update_board(pos)
        game2.swap_player()
    assert game2.check_tie() == True

    game3 = TicTacToe()
    win_possibility = [2,1,3,5,4,9,6]
    for pos in win_possibility:
        game3.update_board(pos)
        game3.swap_player()
    assert game3.check_tie() == False

    game4 = TicTacToe()
    win_possibility = [1,2,3,4,5,6,7,8]
    for pos in win_possibility:
        game4.update_board(pos)
        game4.swap_player()
    assert game4.check_tie() == False


def test_is_running():
    game1 = TicTacToe()
    tie_possibilities = [1,2,3,6,4,7,5,8,9]
    for pos in tie_possibilities:
        game1.update_board(pos)
        game1.swap_player()
    assert game1.is_running() == False

    game2 = TicTacToe()
    win_possibility = [2,1,3,5,4,9,6]
    for pos in win_possibility:
        game2.update_board(pos)
        game2.swap_player() == True
    assert game2.check_win() == True
    assert game2.is_running() == False

    game3 = TicTacToe()
    game3.update_board(2)
    assert game3.is_running() == True
    game3.__init__()
    assert game3.is_running() == True
    
def test_get_board():
    game1 = TicTacToe()
    game1.update_board(20)
    assert game1.get_board() == [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

    game2 = TicTacToe()
    game2.update_board(2)
    modified_board = [['_', 'O', '_'],['_', '_', '_'],['_', '_', '_']]
    assert game2.get_board() == modified_board

    game3 = TicTacToe()
    tie_possibilities = [1,2,3,6,4,7,5,8,9]
    for pos in tie_possibilities:
        game3.update_board(pos)
        game3.swap_player()
    updated_board = game3.get_board()
    assert game3.update_board(2) == False
    assert game3.get_board() == updated_board

    updated_board = game3.get_board()
    assert game3.update_board(20) == False
    assert game3.get_board() == updated_board