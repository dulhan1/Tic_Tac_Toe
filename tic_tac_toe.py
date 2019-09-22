# Tic Tac Toe
# Dulhan

import random
import time

#############################################################################

def Board():
    print(" ", "1", "2", "3")
    print("1",*toplist)
    print("2",*midlist)
    print("3",*bottomlist)
    return

#############################################################################

def WinPlayer1():
    global gameLoop
    global player2Loop
    global lastLoop
    global leaderboard

    gameLoop = False
    player2Loop = False
    lastLoop = False
    win = True

    if toplist.count("X") == 3 or midlist.count("X") == 3 or bottomlist.count("X") == 3:
        print("PLAYER 1 WINS")
    elif toplist[0] == "X" and midlist[0] == "X" and bottomlist[0] == "X":
        print("PLAYER 1 WINS")
    elif toplist[1] == "X" and midlist[1] == "X" and bottomlist[1] == "X":
        print("PLAYER 1 WINS")
    elif toplist[2] == "X" and midlist[2] == "X" and bottomlist[2] == "X":
        print("PLAYER 1 WINS")
    elif toplist[0] == "X" and midlist[1] == "X" and bottomlist[2] == "X":
        print("PLAYER 1 WINS")
    elif toplist[2] == "X" and midlist[1] == "X" and bottomlist[0] == "X":
        print("PLAYER 1 WINS")
    else:
        gameLoop = True
        player2Loop = True
        lastLoop = True
        win = False
    if win:
        name = input("Player 1, please enter you name: ")
        file = open("leaderboard.txt", "a")
        file.writelines(name + "\n")
        file.close()
        file = open("leaderboard.txt", "r")
        leaderboard = file.readlines()
        print("")
        print(*leaderboard)
    return


#############################################################################

def WinPlayer2():
    global gameLoop

    gameLoop = False
    win = True

    if toplist.count("O") == 3 or midlist.count("O") == 3 or bottomlist.count("O") == 3:
        print("PLAYER 2 WINS")
    elif toplist[0] == "O" and midlist[0] == "O" and bottomlist[0] == "O":
        print("PLAYER 2 WINS")
    elif toplist[1] == "O" and midlist[1] == "O" and bottomlist[1] == "O":
        print("PLAYER 2 WINS")
    elif toplist[2] == "O" and midlist[2] == "O" and bottomlist[2] == "O":
        print("PLAYER 2 WINS")
    elif toplist[0] == "O" and midlist[1] == "O" and bottomlist[2] == "O":
        print("PLAYER 2 WINS")
    elif toplist[2] == "O" and midlist[1] == "O" and bottomlist[0] == "O":
        print("PLAYER 2 WINS")
    else:
        gameLoop = True
        win = False
    if win:
        name = input("Player 2, please enter you name: ")
        file = open("leaderboard.txt", "a")
        file.writelines(name + "\n")
        file.close()
        file = open("leaderboard.txt", "r")
        leaderboard = file.readlines()
        print("")
        print(*leaderboard)
    return


#############################################################################

def WinComputer():
    global gameLoop
    global player1Loop
    global level


    gameLoop = False
    player1Loop = True
    win = True

    if toplist.count("O") == 3 or midlist.count("O") == 3 or bottomlist.count("O") == 3:
        print("COMPUTER WINS")
    elif toplist[0] == "O" and midlist[0] == "O" and bottomlist[0] == "O":
        print("COMPUTER WINS")
    elif toplist[1] == "O" and midlist[1] == "O" and bottomlist[1] == "O":
        print("COMPUTER WINS")
    elif toplist[2] == "O" and midlist[2] == "O" and bottomlist[2] == "O":
        print("COMPUTER WINS")
    elif toplist[0] == "O" and midlist[1] == "O" and bottomlist[2] == "O":
        print("COMPUTER WINS")
    elif toplist[2] == "O" and midlist[1] == "O" and bottomlist[0] == "O":
        print("COMPUTER WINS")
    else:
        gameLoop = True
        win = False
    if win:
        name = "Computer Level " + str(level)
        file = open("leaderboard.txt", "a")
        file.writelines(name + "\n")
        file.close()
        file = open("leaderboard.txt", "r")
        leaderboard = file.readlines()
        print("")
        print(*leaderboard)
    return

#############################################################################

def Defense():
    global DefenseCheck
    global DefenseList
    global player2Loop

    DefenseCheck = False
    colLoop = True
    player2Loop = False

    if toplist.count("X") == 2 and toplist.count("O") == 0: # Checks horizontals
        toplist[toplist.index("_")] = "O"
        DefenseCheck = True
        colLoop = False
    elif midlist.count("X") == 2 and midlist.count("O") == 0:
        midlist[midlist.index("_")] = "O"
        DefenseCheck = True
        colLoop = False
    elif bottomlist.count("X") == 2 and bottomlist.count("O") == 0:
        bottomlist[bottomlist.index("_")] = "O"
        DefenseCheck = True
        colLoop = False

    if colLoop:
        c = 0
        while c < 3: # for loop did not work for some reason
            if sum([toplist[c] == "X", midlist[c] == "X", bottomlist[c] == "X"]) == 2: # Checks verticals

                if toplist[c] == "_":
                    toplist[c] = "O"
                    DefenseCheck = True
                    colLoop = False
                    break
                elif midlist[c] == "_":
                    midlist[c] = "O"
                    DefenseCheck = True
                    colLoop = False
                    break
                elif bottomlist[c] == "_":
                    bottomlist[c] = "O"
                    DefenseCheck = True
                    colLoop = False
                    break
                else:
                    c = c + 1
            else:
                c = c + 1

    if colLoop:
        if sum([toplist[0] == "X", midlist[1] == "X", bottomlist[2] == "X"]) == 2:  # Checks one diagonal
            if toplist[0] == "_":
                toplist[0] = "O"
                DefenseCheck = True
                colLoop = False

            elif midlist[1] == "_":
                midlist[1] = "O"
                DefenseCheck = True
                colLoop = False

            elif bottomlist[2] == "_":
                bottomlist[2] = "O"
                DefenseCheck = True
                colLoop = False

    if colLoop:
        if sum([toplist[2] == "X", midlist[1] == "X", bottomlist[0] == "X"]) == 2: # Checks the other diagonal
            if toplist[2] == "_":
                toplist[2] = "O"
                DefenseCheck = True

            elif midlist[1] == "_":
                midlist[1] = "O"
                DefenseCheck = True

            elif bottomlist[0] == "_":
                bottomlist[0] = "O"
                DefenseCheck = True

    return

#############################################################################

def Offense():

    global OffenseCheck
    global player2Loop

    OffenseCheck = False
    colLoop = True
    player2Loop = False

    if toplist.count("O") == 2 and toplist.count("X") == 0: # Checks horizontals
        toplist[toplist.index("_")] = "O"
        OffenseCheck = True
        colLoop = False
    elif midlist.count("O") == 2 and midlist.count("X") == 0:
        midlist[midlist.index("_")] = "O"
        OffenseCheck = True
        colLoop = False
    elif bottomlist.count("O") == 2 and bottomlist.count("X") == 0:
        bottomlist[bottomlist.index("_")] = "O"
        OffenseCheck = True
        colLoop = False

    if colLoop:
        c = 0
        while c < 3: # for loop did not work for some reason
            if sum([toplist[c] == "O", midlist[c] == "O", bottomlist[c] == "O"]) == 2: # Checks verticals

                if toplist[c] == "_":
                    toplist[c] = "O"
                    OffenseCheck = True
                    colLoop = False
                    break
                elif midlist[c] == "_":
                    midlist[c] = "O"
                    OffenseCheck = True
                    colLoop = False
                    break
                elif bottomlist[c] == "_":
                    bottomlist[c] = "O"
                    OffenseCheck = True
                    colLoop = False
                    break
                else:
                    c = c + 1
            else:
                c = c + 1

    if colLoop:
        if sum([toplist[0] == "O", midlist[1] == "O", bottomlist[2] == "O"]) == 2:  # Checks one diagonal
            if toplist[0] == "_":
                toplist[0] = "O"
                OffenseCheck = True
                colLoop = False

            elif midlist[1] == "_":
                midlist[1] = "O"
                OffenseCheck = True
                colLoop = False

            elif bottomlist[2] == "_":
                bottomlist[2] = "O"
                OffenseCheck = True
                colLoop = False

    if colLoop:
        if sum([toplist[2] == "O", midlist[1] == "O", bottomlist[0] == "O"]) == 2: # Checks the other diagonal
            if toplist[2] == "_":
                toplist[2] = "O"
                OffenseCheck = True

            elif midlist[1] == "_":
                midlist[1] = "O"
                OffenseCheck = True

            elif bottomlist[0] == "_":
                bottomlist[0] = "O"
                OffenseCheck = True

    return

#############################################################################

wins = 0
programLoop = True
while programLoop:

    toplist = ["_", "_", "_"]
    midlist = ["_", "_", "_"]
    bottomlist = ["_", "_", "_"]

    print("Menu")
    print("1. One Player (against computer)")
    print("2. Two Player")
    print("3. Exit")

    text = input("Please choose an option (1 or 2): ")

    gameLoop = True

#-----------------------------------------------------------------------------------------------------------------------

    if text == "1":
        print("1. Level 1")
        print("2. Level 2")
        print("3. Level 3")
        textcomp = input("Please choose an option (1, 2, or 3): ")
        if textcomp == "1":                                                         # Level 1 Computer - Random
            level = 1
            move = input("Do you want to go first or second (f or s): ")
            if move == "s":
                player1Loop = False
                firstLoop = False
                player2Loop = True
                lastLoop = True

            elif move == "f":
                firstLoop = True
                player1Loop = True

            Board()
            while (toplist.count("_") != 0 or midlist.count("_") != 0 or bottomlist.count("_") != 0) and gameLoop == True:

                while player1Loop:
                    row = int(input("Input row (1, 2, or 3): "))
                    col = int(input("Input Column (1, 2, or 3): "))
                    if row == 1 and toplist[col - 1] == "_":
                        toplist[col - 1] = "X"
                        firstLoop = True
                        break

                    elif row == 2 and midlist[col - 1] == "_":
                        midlist[col - 1] = "X"
                        firstLoop = True
                        break

                    elif row == 3 and bottomlist[col - 1] == "_":
                        bottomlist[col - 1] = "X"
                        firstLoop = True
                        break

                    else:
                        print("That position is taken up! Please try again")
                        player1Loop = True
                        player2Loop = False
                        firstLoop = False

                if firstLoop:
                    print("Your move was: ")
                    Board()
                    WinPlayer1()

                if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count(
                        "_") == 0 and gameLoop == True:
                    print("The game is a draw!")
                    player2Loop = False
                    lastLoop = False

                while player2Loop:
                    row = random.randint(1, 3)
                    col = random.randint(1, 3)

                    if row == 1 and toplist[col - 1] == "_":
                        toplist[col - 1] = "O"
                        break
                    elif row == 2 and midlist[col - 1] == "_":
                        midlist[col - 1] = "O"
                        break
                    elif row == 3 and bottomlist[col - 1] == "_":
                        bottomlist[col - 1] = "O"
                        break
                    else:
                        player2Loop = True
                if lastLoop:
                    print("Computer's move was: ")
                    time.sleep(1)
                    Board()
                    WinComputer()

                if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count(
                        "_") == 0 and gameLoop == True:
                    print("The game is a draw!")
                    player2Loop = False

# -----------------------------------------------------------------------------------------------------------------------

        if textcomp == "2":                                                          # Level 2 Computer - Plays Defense
            level = 2
            move = input("Do you want to go first or second (f or s): ")
            if move == "s":
                player1Loop = False
                firstLoop = False
                player2Loop = True
                lastLoop = True

            elif move == "f":
                firstLoop = True
                player1Loop = True

            Board()
            while (toplist.count("_") != 0 or midlist.count("_") != 0 or bottomlist.count("_") != 0) and gameLoop == True:

                while player1Loop:
                    row = int(input("Input row (1, 2, or 3): "))
                    col = int(input("Input Column (1, 2, or 3): "))
                    if row == 1 and toplist[col - 1] == "_":
                        toplist[col - 1] = "X"
                        firstLoop = True
                        break

                    elif row == 2 and midlist[col - 1] == "_":
                        midlist[col - 1] = "X"
                        firstLoop = True
                        break

                    elif row == 3 and bottomlist[col - 1] == "_":
                        bottomlist[col - 1] = "X"
                        firstLoop = True
                        break

                    else:
                        print("That position is taken up! Please try again")
                        player1Loop = True
                        player2Loop = False
                        firstLoop = False

                if firstLoop:
                    print("Your move was: ")
                    Board()
                    WinPlayer1()

                if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count(
                        "_") == 0 and gameLoop == True:
                    print("The game is a draw!")
                    player2Loop = False
                    lastLoop = False

                while player2Loop:

                    Defense()

                    if not DefenseCheck:
                        row = random.randint(1, 3)
                        col = random.randint(1, 3)

                        if row == 1 and toplist[col - 1] == "_":
                            toplist[col - 1] = "O"
                            break
                        elif row == 2 and midlist[col - 1] == "_":
                            midlist[col - 1] = "O"
                            break
                        elif row == 3 and bottomlist[col - 1] == "_":
                            bottomlist[col - 1] = "O"
                            break
                        else:
                            player2Loop = True
                if lastLoop:
                    print("Computer's move was: ")
                    time.sleep(1)
                    Board()
                    WinComputer()

                if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count(
                        "_") == 0 and gameLoop == True:
                    print("The game is a draw!")
                    player2Loop = False

# -----------------------------------------------------------------------------------------------------------------------

        if textcomp == "3":                                              # Level 3 Computer - Plays defense and offense
            level = 3                                                    # There is only one way to beat computer Level 3
            move = input("Do you want to go first or second (f or s): ")
            if move == "s":
                player1Loop = False
                firstLoop = False
                player2Loop = True
                lastLoop = True

            elif move == "f":
                firstLoop = True
                player1Loop = True

            Board()
            while (toplist.count("_") != 0 or midlist.count("_") != 0 or bottomlist.count(
                    "_") != 0) and gameLoop == True:

                while player1Loop:
                    row = int(input("Input row (1, 2, or 3): "))
                    col = int(input("Input Column (1, 2, or 3): "))
                    if row == 1 and toplist[col - 1] == "_":
                        toplist[col - 1] = "X"
                        firstLoop = True
                        break

                    elif row == 2 and midlist[col - 1] == "_":
                        midlist[col - 1] = "X"
                        firstLoop = True
                        break

                    elif row == 3 and bottomlist[col - 1] == "_":
                        bottomlist[col - 1] = "X"
                        firstLoop = True
                        break

                    else:
                        print("That position is taken up! Please try again")
                        player1Loop = True
                        player2Loop = False
                        firstLoop = False

                if firstLoop:
                    print("Your move was: ")
                    Board()
                    WinPlayer1()

                if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count(
                        "_") == 0 and gameLoop == True:
                    print("The game is a draw!")
                    player2Loop = False


                while player2Loop:

                    if ((toplist.count("X") + midlist.count("X") + bottomlist.count("X")) == 1) and midlist[1] != "X":
                        midlist[1] = "O"
                        player2Loop = False
                    elif ((toplist.count("X") + midlist.count("X") + bottomlist.count("X")) == 0):
                        numList = [1,3]
                        row = random.choice(numList)
                        col = random.choice(numList)
                        if row == 1 and toplist[col - 1] == "_":
                            toplist[col - 1] = "O"
                        elif row == 3 and bottomlist[col - 1] == "_":
                            bottomlist[col - 1] = "O"
                        player2Loop = False

                    else:

                        Offense()

                        if not OffenseCheck:

                            Defense()

                        if not DefenseCheck and not OffenseCheck:

                            row = random.randint(1,3)
                            col = random.randint(1,3)

                            if row == 1 and toplist[col - 1] == "_":
                                toplist[col - 1] = "O"
                                break
                            elif row == 2 and midlist[col - 1] == "_":
                                midlist[col - 1] = "O"
                                break
                            elif row == 3 and bottomlist[col - 1] == "_":
                                bottomlist[col - 1] = "O"
                                break
                            else:
                                player2Loop = True
                if lastLoop:
                    print("Computer's move was: ")
                    time.sleep(1)
                    Board()
                    WinComputer()

                if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count(
                        "_") == 0 and gameLoop == True:
                    print("The game is a draw!")
                    player2Loop = False
# -----------------------------------------------------------------------------------------------------------------------

    if text == "2":
        Board()
        while (toplist.count("_") != 0 or midlist.count("_") != 0 or bottomlist.count("_") != 0) and gameLoop == True:
            player1Loop = True
            while player1Loop:

                print("")
                print("Player 1")
                row = int(input("Input row (1, 2, or 3): "))
                col = int(input("Input Column (1, 2, or 3): "))
                if row == 1 and toplist[col - 1] == "_":
                    toplist[col - 1] = "X"
                    break
                elif row == 2 and midlist[col - 1] == "_":
                    midlist[col - 1] = "X"
                    break
                elif row == 3 and bottomlist[col - 1] == "_":
                    bottomlist[col - 1] = "X"
                    break
                else:
                    print("That position is taken up! Please try again")
                    player1Loop = True
                    player2Loop = False
            print("Your move was: ")
            Board()
            WinPlayer1()
            if toplist.count("_") == 0 and midlist.count("_") == 0 and bottomlist.count("_") == 0 and gameLoop == True:
                print("The game is a draw!")
                player2Loop = False
                gameLoop = False

            while player2Loop:

                print("")
                print("Player 2")
                row = int(input("Input row (1, 2, or 3): "))
                col = int(input("Input Column (1, 2, or 3): "))
                if row == 1 and toplist[col - 1] == "_":
                    toplist[col - 1] = "O"
                    break
                elif row == 2 and midlist[col - 1] == "_":
                    midlist[col - 1] = "O"
                    break
                elif row == 3 and bottomlist[col - 1] == "_":
                    bottomlist[col - 1] = "O"
                    break
                else:
                    print("That position is taken up!")
            if lastLoop:
                print("Your move was: ")
                Board()
                WinPlayer2()

    if text == "3":
        print("program Exiting...")
        programLoop = False

input("Press enter to continue")
