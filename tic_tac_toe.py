"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""

import random

def greet_user() -> None:
    greeting = "Welcome to Tic Tac Toe"
    separator = "=" * 40
    print(greeting, separator, sep= "\n")

def print_game_rules() -> None:
    game_rules = """
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""" 
    separator = "=" * 40
    print(game_rules, separator, sep= "\n")

def start_game() -> None:
    """ Print a start message."""
    message = "Let's start the game"  
    separator = "_" * 40
    print(message, separator, sep= "\n")  

def choose_player() -> dict: #osetrit validitu vstupu
    players = dict()
    player_x = input('Name of player x, "c" for computer:')
    players["x"] = player_x
    player_o = input('Name of player o, "c" for computer:')
    players["o"] = player_o
    return players #jmeno hrace nebo c

def print_game_board(board: list) -> None:
    """ Print a game board.
    Parameters:
    - board: A list representing a game board."""
   
    grid = "+---+---+---+"
    print(grid)
    for row in board:
        print("|", end= " ")
        for cell in row:
            print(cell, end= " | ")
        print("\n" + grid) 

def switch_player(active_player = "x") -> str: 
    """Switch between players each round.
    Parameters:
    - player: Active player."""
    return "x" if active_player == "o" else "o"

def get_move_number(players, active_player) -> int: 
    """Return a number of cell from active user input.
    Check input validity.
    Parameters:
    - player: Active player."""    
    
    while True:
        if players[active_player] == "c":
            move = random.randint(1, 9)
            return move

        else:
            try:
                move = int(input(f"""
Player {active_player} | Please enter your move number (1-9):"""))
                if move in range(1,10):
                    return move
                else: 
                    raise ValueError ("Please enter a number between 1 and 9.")     
            except ValueError:
                print("That's not a number.")

def make_move(board: list, active_player: str, move: int, players: dict) -> list[str]:
    """Make a move on a game board.
    Parameters:
    - board: A list representing a game board.
    - player: Player "o" or player "x".
    - move: Place a stone "o"/"x" in a cell number 1 - 9. """
     
    while True:
        row = (move - 1) // 3
        cell = (move - 1) % 3
        if board[row][cell] == " ":
            board[row][cell] = active_player
            print_game_board(board)
            return board
        else:
            print_game_board(board)
            if players[active_player] != "c":
                print("This cell is already occupied.")
            move = get_move_number(players, active_player)
          
def validate_board(board: list, active_player: str) -> bool:             
    """Check game status.
    Parameters:
    - board: A list representing a game board.
    - player: Active player."""

    for row in board: # winning rows
        if row[0] == row[1] == row[2] != " ":
            print(f"Player {active_player}, has won!")
            return False
    for cell in range(3): #winning columns
            if board[0][cell] == board[1][cell] == board[2][cell] != " ":
                print(f"Player {active_player} has won!") 
                return False
    if board[0][0] == board[1][1] == board[2][2] != " ": #winning diagonals
        print(f"Player {active_player} has won!")
        return False
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"Player {active_player} has won!") 
        return False
   

def main():
    greet_user()
    print_game_rules()
    start_game()
    players = choose_player()

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    active_player = "x"
    print_game_board(board) 

    while True:
        active_player = switch_player(active_player)  
        move = get_move_number(players, active_player) 
        board = make_move(board, active_player, move, players)
        if validate_board(board, active_player) == False:
            break
        
if __name__ == "__main__":
    main()