#
# #Algorithm
#
# '''#--->create board
# #--->two players
# #--->flip(swap) players
# -->check who is the winner
#    -->rows(3)
#    -->columns(3)
#    -->diagonals(2)
# -->drawn'''
#
# #player-->X
# #player2-->O
#
# #creation of the board
# board=["-","-","-",
#        "-","-","-",
#        "-","-","-"]
#
# current_player="X"
# gameisgoing=True
# winner=None
# def display_board():
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print(board[6] + " | " + board[7] + " | " + board[8])
#
# def handle_turn():
#     position=int(input("Choose a random position from 0 to 8:"))#0
#     if position<8:
#         board[position] = current_player


#     if position>8:
#         position = int(input("Choose a random position from 0 to 8:"))
#
#     board[position] = current_player
#
# def swap_players():
#     global current_player
#     if current_player=="X":
#         current_player="O"
#     elif current_player=="O":
#         current_player="X"
#
# def check_who_is_the_winner():
#     global winner
#     rowwinner=check_row()
#     colwinner=check_column()
#     diawinner=check_diagonal()
#     check_tie()
#
#     if rowwinner:
#         winner=rowwinner
#     elif colwinner:
#         winner=colwinner
#     else:
#         winner=diawinner
#
# def check_row():
#
#     global gameisgoing
#    #player can win in three rows
#     row1 = board[0] == board[1] == board[2] != "-"#either X or O,X
#     row2 = board[3] == board[4] == board[5] != "-"#either X or O,X
#     row3 = board[6] == board[7] == board[8] != "-"#either X or O#X
#
#     if row1 or row2 or row3:
#         gameisgoing=False
#
#
#     if row1:#in row1 if some thing is present
#      return board[0]
#
#     elif row2:
#      return board[5]
#
#     elif row3:
#      return board[6]
#
#
# def check_column():
#     global gameisgoing
#     # player can win in three rows
#     col1 = board[0] == board[3] == board[6] != "-"  # either X or O,X
#     col2 = board[1] == board[4] == board[7] != "-"  # either X or O,X
#     col3 = board[2] == board[5] == board[8] != "-"  # either X or O#X
#
#     if col1 or col2 or col3:
#         gameisgoing = False
#
#     if col1:  # in row1 if some thing is present
#         return board[0]
#
#     elif col2:
#         return board[1]
#
#     elif col3:
#         return board[5]
#
# def check_diagonal():
#     global gameisgoing
#     # player can win in three rows
#     dia1 = board[0] == board[4] == board[8] != "-"  # either X or O,X
#     dia2 = board[2] == board[4] == board[6] != "-"  # either X or O,X
#
#
#     if dia1 or dia2:
#         gameisgoing = False
#
#     if dia1:  # in row1 if some thing is present
#         return board[0]
#
#     elif dia2:
#         return board[4]
#
# def check_tie():
#     global gameisgoing
#     if "-" not in board:
#         gameisgoing=False
#         print("Match is Tied")
#
# def play_game():
#     while gameisgoing:
#         display_board()
#
#         handle_turn()
#
#         swap_players()
#
#         check_who_is_the_winner()
#
#     if winner=="X":
#         print("X is the winner")
#     elif winner=="O":
#         print("O is the winner")
#
# play_game()
#
#
#
#
#
#

import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

########win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################
Game = Running
Mark = 'X'


# This Function Draws Game Board
def DrawBoard():
    print(" %c| %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# This Function Checks position is empty or not
def CheckPosition(x):
    if (board[x] == ' '):
        return True
    else:
        return False

    # This Function Checks player has won or not


def CheckWin():
    global Game
    # Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
        # Vertical Winning Condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
        # Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
        # Match Tie or Draw Condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game Designed By Tillotama")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)
while (Game == Running):
    os.system('cls')
    DrawBoard()
    if (player % 2 != 0):
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if (CheckPosition(choice)):
        board[choice] = Mark
        player += 1
        CheckWin()

os.system('cls')
DrawBoard()
if (Game == Draw):
    print("Game Draw")
elif (Game == Win):
    player -= 1
    if (player % 2 != 0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")





