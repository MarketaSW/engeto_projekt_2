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

def print_game_board(board):
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
    return board    

def get_move_number(player = "x"):
    while game_on:
        if player == "o":
            player = "x"
        else:
            player = "o" 

        move_number = input(f"""
Player {player} | Please enter your move number(1-9):""")
        if move_number.isdigit():
            move = int(move_number)
            if move in range(1,10):
                return move
            else:
                print("Please enter a number between 1 and 9.")    
        else:
            print("That's not a number.")         

def make_move(board, player, move): #check if the board is full / s/o won
    """ Make a move on a game board.
    Parameters:
    - board: A list representing a game board.
    - player: Player "o" or player "x".
    - move: Place a stone "o"/"x" in a cell number 1 - 9. """
    while game_on:
        row = ((move - 1) // 3)
        cell = ((move - 1) % 3)
        if board[row][cell] == "   ":
            board[row][cell] = player 
        elif " " not in board:
            game_on = False
            print("Game over!")
        else:
            print("This slot is already occupied.") 

        for row in board: # winning rows
            if row[0] == row[1] == row[2] != " ":
                game_on = False
                print(f"Player {player} has won!")
        for cell in range(3): #winning columns
            if board[0][cell] == board[1][cell] == board[2][cell] != " ":
                game_on = False
                print(f"Player {player} has won!") #winning diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            game_on = False
            print(f"Player {player} has won!") 

        return board          
    
def main():
    game_on = True
    greet_user()
    print_game_rules()
    print_start_game()
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    print_game_board(board)
    get_move_number()
    make_move(board, player, move)

main()    
