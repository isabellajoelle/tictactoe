"""
Title: Tic Tac Toe
Author: Isabella Cruz

"""

start_board ="""

            |       |       
        1   |   2   |   3
            |       |
    -------------------------
            |       |       
        4   |   5   |   6
            |       |
    -------------------------
            |       |       
        7   |   8   |   9
            |       |
            
    """

def intro():
    print()
    print("------------ Welcome! -------------")
    print()
    print(start_board)      
    print("  Player 1 = X's    Player 2 = O's")
    print()
    if wantAI():
        print()
        print("          YOU ARE PLAYER 1        ")
        OnePlayerGame(start_board, [1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    else: TwoPlayerGame(start_board, [1, 2, 3, 4, 5, 6, 7, 8, 9], 1)

def moveString(player):
    print()
    print("------------ PLAYER " + str(player) + " -------------")

def TwoPlayerGame(game_board, board_tracker, player):
    moveString(player)
    move = input("Enter Move #: ")
    while(not MoveValidityChecker(move, board_tracker)):
        move = input("Enter Move #: ")
    new_board = boardUpdater(game_board, move, player)
    print(new_board)
    if player == 1: board_tracker[int(move)-1] = True
    else: board_tracker[int(move)-1] = False
    if endgame_checker(board_tracker) == "WIN": win(player)
    elif endgame_checker(board_tracker) == "TIE": tie()
    else:
        if player == 1: TwoPlayerGame(new_board, board_tracker, 2)
        else: TwoPlayerGame(new_board, board_tracker, 1) 

def OnePlayerGame(game_board, board_tracker, player):
    moveString(player)
    if player == 2:
        AI_move = makeAImove(game_board, board_tracker)
        print(AI_move[0])
        print("           Move Made: " + str(AI_move[1]+1))
    else:
        move = input("Enter Move #: ")
        while(not MoveValidityChecker(move, board_tracker)):
            move = input("Enter Move #: ")
        new_board = boardUpdater(game_board, move, 1)
        print(new_board)
    if player == 1: board_tracker[int(move)-1] = True
    else: board_tracker[AI_move[1]] = False
    if endgame_checker(board_tracker) == "WIN": win(player)
    elif endgame_checker(board_tracker) == "TIE": tie()
    else:
        if player == 1: OnePlayerGame(new_board, board_tracker, 2)
        else: OnePlayerGame(AI_move[0], board_tracker, 1)

def wantAI():
    answer = input("         1 or 2 Players?: ")
    try:
        ans = int(answer)
        if int(ans) == 1: return True
        if int(ans) == 2: return False
        else:
            print(" *** ERROR: Must enter '1' or '2' ***")
            return wantAI()
    except ValueError:
        print("* ERROR: Must enter ints '1' or '2' *")
        return wantAI()
            
def MoveValidityChecker(move, board_tracker):
    try:
        move = int(move)
        if move > 9 or move < 1:
            print("ERROR: Move must be a position between 1-9")
            return False
        elif type(board_tracker[move-1]) != int: 
            print("ERROR: That spot is already taken")
            return False
        else: return True
    except ValueError:
        print("ERROR: Must enter a number (1-9)")
        return False   

def boardUpdater(current_board, position, player):
    if player == 1: return current_board.replace(position,"X") 
    else: return current_board.replace(position,"O")

def makeAImove(game_board, BT):
    #checks for 2 in a row
    if two_checker(0, 1, 2, BT) < 10: return [boardUpdater(game_board, str(two_checker(0, 1, 2, BT)), 2), two_checker(0, 1, 2, BT)-1]
    if two_checker(3, 4, 5, BT) < 10: return [boardUpdater(game_board, str(two_checker(3, 4, 5, BT)), 2), two_checker(3, 4, 5, BT)-1]
    if two_checker(6, 7, 8, BT) < 10: return [boardUpdater(game_board, str(two_checker(6, 7, 8, BT)), 2), two_checker(6, 7, 8, BT)-1]
    if two_checker(0, 3, 6, BT) < 10: return [boardUpdater(game_board, str(two_checker(0, 3, 6, BT)), 2), two_checker(0, 3, 6, BT)-1]
    if two_checker(1, 4, 7, BT) < 10: return [boardUpdater(game_board, str(two_checker(1, 4, 7, BT)), 2), two_checker(1, 4, 7, BT)-1]
    if two_checker(2, 5, 8, BT) < 10: return [boardUpdater(game_board, str(two_checker(2, 5, 8, BT)), 2), two_checker(2, 5, 8, BT)-1]
    if two_checker(0, 4, 8, BT) < 10: return [boardUpdater(game_board, str(two_checker(0, 4, 8, BT)), 2), two_checker(0, 4, 8, BT)-1]
    if two_checker(2, 4, 6, BT) < 10: return [boardUpdater(game_board, str(two_checker(2, 4, 6, BT)), 2), two_checker(2, 4, 6, BT)-1]
    #take middle if open
    if type(BT[4]) == int: return [boardUpdater(game_board, "5", 2), 4]
    #prevents open corner trap
    if BT[1] == BT[3] and type(BT[1]) == bool:
        if type(BT[0]) == int: return [boardUpdater(game_board, "1", 2), 0]
    if BT[3] == BT[7] and type(BT[3]) == bool:
        if type(BT[6]) == int: return [boardUpdater(game_board, "7", 2), 6]
    if BT[1] == BT[5] and type(BT[1]) == bool:
        if type(BT[2]) == int: return [boardUpdater(game_board, "3", 2), 2]
    if BT[7] == BT[5] and type(BT[5]) == bool:
        if type(BT[8]) == int: return [boardUpdater(game_board, "9", 2), 8]
    #prevents corner trap
    if BT[4] == False and type(BT[1]) == int: return [boardUpdater(game_board, "2", 2), 1]
    if BT[0] == BT[8] and type(BT[0]) == bool:
        if type(BT[2]) == int: return [boardUpdater(game_board, "3", 2), 2]
        if type(BT[6]) == int: return [boardUpdater(game_board, "7", 2), 6]
    if BT[2] == BT[6] and type(BT[2]) == bool:
        if type(BT[0]) == int: return [boardUpdater(game_board, "1", 2), 0]
        if type(BT[8]) == int: return [boardUpdater(game_board, "9", 2), 8]
    else:
        for i in range(9):
            if type(BT[i]) == int:
                move = i
                break
        return [boardUpdater(game_board, str(move+1), 2), move]
        
def two_checker(pos1, pos2, pos3, BT):
    if type(BT[pos1]) == bool and type(BT[pos2]) == bool and type(BT[pos3])== bool: return 10
    if BT[pos1] == BT[pos2] and type(BT[pos1]) == bool:
        if type(BT[pos3]) == int: return BT[pos3]
    if BT[pos2] == BT[pos3] and type(BT[pos2]) == bool:
        if type(BT[pos1]) == int: return BT[pos1]
    if BT[pos1] == BT[pos3] and type(BT[pos1]) == bool:
        if type(BT[pos2]) == int: return BT[pos2]
    else: return 10

def endgame_checker(BT):
    if (BT[0] == BT[1] and BT[1] == BT[2]) or (BT[3] == BT[4] and BT[4] == BT[5]) or (BT[6] == BT[7] and BT[7] == BT[8]): return "WIN"
    elif (BT[0] == BT[3] and BT[3] == BT[6]) or (BT[1] == BT[4] and BT[4] == BT[7]) or (BT[2] == BT[5] and BT[5] == BT[8]): return "WIN"
    elif (BT[0] == BT[4] and BT[4] == BT[8]) or (BT[2] == BT[4] and BT[4] == BT[6]): return "WIN"
    else:
        tracker = True
        for i in range(len(BT)):
            tracker += 1
            if type(BT[i]) == int:
                tracker = False
                break
        if tracker: return "TIE"
        else: return "NONE"
        
def play_again():
    answer = input("Would you like to play again (Y/N): ")
    if answer == "Y" or answer == "y": return intro()
    if answer == "N" or answer == "n":
        print()
        print("******** THANKS FOR PLAYING! ********")
    else:
        print("ERROR: Respond with 'Y' or 'N'")
        return play_again()
    
def win(player):
    print("*************************************")
    print("*--------- PLAYER " + str(player) + " WINS -----------*")
    print("*************************************")
    print()
    play_again()

def tie():
    print("*************************************")
    print("*----------- ITS A TIE! ------------*")
    print("*************************************")
    print()
    play_again()  

intro()
