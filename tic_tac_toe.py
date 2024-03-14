"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""
game_on = True
def greet_user():
    greeting = "Welcome to Tic Tac Toe"
    separator = "=" * 40
    print(greeting, separator, sep= "\n")

def print_game_rules():
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

def print_start_game():
    message = "Let's start the game"  
    separator = "_" * 40
    print(message, separator, sep= "\n")  

def print_game_board():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    grid = "+---+---+---+"
    print(grid)
    for row in board:
        print("|", end= "")
        for cell in row:
            cell = "   "
            print(cell, end= "|")
        print("\n" + grid)
    return board    

def get_move_number(player = "x"):
    while game_on:
        move = input(f"Player {player} | Please enter your move number:")
        if player == "o":
            player = "x"
        else:
            player = "o"    
    return move

def make_move(board, player, move):
    """ Make a move on a game board.
    Parameters:
    - board: A list representing a game board.
    - player: Player "o" or player "x".
    - move: Place a stone "o"/"x" in a cell number 1 - 9. """
    row = ((move - 1) // 3)
    cell = ((move - 1) % 3)
    if board[row][cell] == "   ":
        board[row][cell] = player 
    else:
        print("This slot is already occupied.") 
    return board          
    
def main():
    game_on = True
    greet_user()
    print_game_rules()
    print_start_game()
    print_game_board()
    get_move_number()
    make_move(board,x,3)

main()    
