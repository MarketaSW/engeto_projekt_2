"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""

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

def switch_player(player = "x") -> str: 
    """Switch between players each round.
    Parameters:
    - player: Active player."""
    return "x" if player == "o" else "o"

def get_move_number(player) -> int: #co když jeden hráč bude počítač?
    """Return a number of cell from active user input.
    Check input validity.
    Parameters:
    - player: Active player."""
    
#     while True:
#         move_number = input(f"""
# Player {player} | Please enter your move number(1-9):""")
#         if move_number.isdigit():
#             move = int(move_number)
#             if move in range(1,10):
#                 return move
#             else:
#                 print("Please enter a number between 1 and 9.")    
#         else:
#             print("That's not a number.")      
    
    # if player == "computer":
    #     (...)
    # elif:
        try:
            move = int(input(f"""
Player {player} | Please enter your move number (1-9):""")
            if move in range(1,10):
                return move
            else: print("Please enter a number between 1 and 9.")     
        except ValueError:
            print("That's not a number.")


#             try:
#     cislo = int(input("Zadej libovolne cislo:"))
#     print(100 / cislo)
# # ConnectionError
# except ValueError:
#     defaultni_cislo = 1
#     print(100 / defaultni_cislo)
#     print(f"Bohuzel jsi nezadal cislo :(")
# except ZeroDivisionError:
#     print(f"Nulou nemuzes delit :9")
# else:
#     print("Pokracujeme dal..")
# finally:
#     print("Ukoncuji zapis")           

def make_move(board: list, player: str, move: int) -> list:
    """Make a move on a game board.
    Parameters:
    - board: A list representing a game board.
    - player: Player "o" or player "x".
    - move: Place a stone "o"/"x" in a cell number 1 - 9. """
     
    while True:
        row = (move - 1) // 3
        cell = (move - 1) % 3
        if board[row][cell] == " ":
            board[row][cell] = player
            print_game_board(board)
            return board
        else:
            print_game_board(board)
            print("This cell is already occupied.")
            move = get_move_number(player)
          
def validate_board(board: list, player: str) -> bool:             
    """Check game status.
    Parameters:
    - board: A list representing a game board.
    - player: Active player."""

    for row in board: # winning rows
        if row[0] == row[1] == row[2] != " ":
            print(f"Player {player} has won!")
            return False
    for cell in range(3): #winning columns
            if board[0][cell] == board[1][cell] == board[2][cell] != " ":
                print(f"Player {player} has won!") 
                return False
    if board[0][0] == board[1][1] == board[2][2] != " ": #winning diagonals
        print(f"Player {player} has won!")
        return False
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"Player {player} has won!") 
        return False
   

def main():
    greet_user()
    print_game_rules()
    start_game()

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    player = "x" 
    print_game_board(board) 

    while True:
        player = switch_player(player)  
        move = get_move_number(player) 
        board = make_move(board, player, move)
        if validate_board(board, player) == False:
            break
        
if __name__ == "__main__":
    main()