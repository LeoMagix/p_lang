"""
Simple Python that creates the preliminary for a Tic-Tac-Toe game.
Some features I would like to add, subsequently:
    >> Announce when we have a winner or a tie.
    >> Prevent a plyer from choosing a positon already chozen by another player.
    >> A mini annoucement at the start with info on how to place postions.
    >> Check/handle invalid input.
"""

theboard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'bot-L':' ', 'bot-M':' ', 'bot-R':' '}

#Function to handle display of tic-tac-toe grid to the screen
def printBoard(board):
    """Describes how the inputs are going to be represented."""
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print("-+-+-")
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print(f"-+-+-")
    print(f"{board['bot-L']}|{board['bot-M']}|{board['bot-R']}")

turn = 'X'
for i in range(9):
    printBoard(theboard)            #This helps display the current situation of the board
    print(f"It's your turn to move Player:{turn}")
    move = input()
    theboard[move] = turn.upper()
    if turn.upper() == 'X':             #sets variable turn to 'O' after player X chooses
        turn = 'O'
    else:
        turn = 'X'                      #Assigns X to the variable turn after player O chooses

printBoard(theboard)
