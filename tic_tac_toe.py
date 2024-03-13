"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""

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
    grid = "+---+---+---+"
    print(grid)
    for row in board:
        print("|", end= "")
        for cell in row:
            cell = "   "
            print(cell, end= "|")
        print("\n" + grid)
       
    

greet_user()
print_game_rules()
print_start_game()
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
print_game_board(board)
