from tkinter import *

master = Tk()
import random

toplist = ["_", "_", "_"]
midlist = ["_", "_", "_"]
bottomlist = ["_", "_", "_"]
var = "True"
level = 0
firstmove = True
draw = False
cPlay = True
letter = "X"
TwoP = False
win = False
winP = False
second = False
################################################################################################
def Offense():
    global OffenseCheck
    global player2Loop

    OffenseCheck = False
    colLoop = True
    player2Loop = False

    if toplist.count("O") == 2 and toplist.count("X") == 0:  # Checks horizontals
        w.create_oval(100 * (toplist.index("_") + 1), 100, 100 * (toplist.index("_") + 2), 200)
        toplist[toplist.index("_")] = "O"
        OffenseCheck = True
        colLoop = False
    elif midlist.count("O") == 2 and midlist.count("X") == 0:
        w.create_oval(100 * (midlist.index("_") + 1), 200, 100 * (midlist.index("_") + 2), 300)
        midlist[midlist.index("_")] = "O"
        OffenseCheck = True
        colLoop = False
    elif bottomlist.count("O") == 2 and bottomlist.count("X") == 0:
        w.create_oval(100 * (bottomlist.index("_") + 1), 300, 100 * (bottomlist.index("_") + 2), 400)
        bottomlist[bottomlist.index("_")] = "O"
        OffenseCheck = True
        colLoop = False

    if colLoop:
        c = 0
        while c < 3:
            if sum([toplist[c] == "O", midlist[c] == "O", bottomlist[c] == "O"]) == 2:

                if toplist[c] == "_":
                    toplist[c] = "O"
                    w.create_oval(100 * (c + 1), 100, 100 * (c + 2), 200)
                    OffenseCheck = True
                    colLoop = False
                    break
                elif midlist[c] == "_":
                    midlist[c] = "O"
                    w.create_oval(100 * (c + 1), 200, 100 * (c + 2), 300)
                    OffenseCheck = True
                    colLoop = False
                    break
                elif bottomlist[c] == "_":
                    bottomlist[c] = "O"
                    w.create_oval(100 * (c + 1), 300, 100 * (c + 2), 400)
                    OffenseCheck = True
                    colLoop = False
                    break
                else:
                    c = c + 1
            else:
                c = c + 1

    if colLoop:
        if sum([toplist[0] == "O", midlist[1] == "O", bottomlist[2] == "O"]) == 2:
            if toplist[0] == "_":
                toplist[0] = "O"
                w.create_oval(100 * (1), 100, 100 * (2), 200)
                OffenseCheck = True
                colLoop = False

            elif midlist[1] == "_":
                midlist[1] = "O"
                w.create_oval(100 * (2), 200, 100 * (3), 300)
                OffenseCheck = True
                colLoop = False

            elif bottomlist[2] == "_":
                bottomlist[2] = "O"
                w.create_oval(100 * (3), 300, 100 * (4), 400)
                OffenseCheck = True
                colLoop = False

    if colLoop:
        if sum([toplist[2] == "O", midlist[1] == "O", bottomlist[0] == "O"]) == 2:
            if toplist[2] == "_":
                toplist[2] = "O"
                w.create_oval(100 * (3), 100, 100 * (4), 200)
                OffenseCheck = True

            elif midlist[1] == "_":
                midlist[1] = "O"
                w.create_oval(100 * (2), 200, 100 * (3), 300)
                OffenseCheck = True

            elif bottomlist[0] == "_":
                bottomlist[0] = "O"
                w.create_oval(100 * (1), 300, 100 * (2), 400)
                OffenseCheck = True

    return
################################################################################################
def Defense():
    global DefenseCheck
    global DefenseList
    global player2Loop

    DefenseCheck = False
    colLoop = True
    player2Loop = False

    if toplist.count("X") == 2 and toplist.count("O") == 0:
        w.create_oval(100 * (toplist.index("_") + 1), 100, 100 * (toplist.index("_") + 2), 200)
        toplist[toplist.index("_")] = "O"
        DefenseCheck = True
        colLoop = False
    elif midlist.count("X") == 2 and midlist.count("O") == 0:
        w.create_oval(100 * (midlist.index("_") + 1), 200, 100 * (midlist.index("_") + 2), 300)
        midlist[midlist.index("_")] = "O"
        DefenseCheck = True
        colLoop = False
    elif bottomlist.count("X") == 2 and bottomlist.count("O") == 0:
        w.create_oval(100 * (bottomlist.index("_") + 1), 300, 100 * (bottomlist.index("_") + 2), 400)
        bottomlist[bottomlist.index("_")] = "O"
        DefenseCheck = True
        colLoop = False

    if colLoop:
        c = 0
        while c < 3:
            if sum([toplist[c] == "X", midlist[c] == "X", bottomlist[c] == "X"]) == 2:

                if toplist[c] == "_":
                    toplist[c] = "O"
                    w.create_oval(100 * (c + 1), 100, 100 * (c + 2), 200)
                    DefenseCheck = True
                    colLoop = False
                    break
                elif midlist[c] == "_":
                    midlist[c] = "O"
                    w.create_oval(100 * (c + 1), 200, 100 * (c + 2), 300)
                    DefenseCheck = True
                    colLoop = False
                    break
                elif bottomlist[c] == "_":
                    bottomlist[c] = "O"
                    w.create_oval(100 * (c + 1), 300, 100 * (c + 2), 400)
                    DefenseCheck = True
                    colLoop = False
                    break
                else:
                    c = c + 1
            else:
                c = c + 1

    if colLoop:
        if sum([toplist[0] == "X", midlist[1] == "X", bottomlist[2] == "X"]) == 2:
            if toplist[0] == "_":
                toplist[0] = "O"
                w.create_oval(100 * (1), 100, 100 * (2), 200)
                DefenseCheck = True
                colLoop = False

            elif midlist[1] == "_":
                midlist[1] = "O"
                w.create_oval(100 * (2), 200, 100 * (3), 300)
                DefenseCheck = True
                colLoop = False

            elif bottomlist[2] == "_":
                bottomlist[2] = "O"
                w.create_oval(100 * (3), 300, 100 * (4), 400)
                DefenseCheck = True
                colLoop = False

    if colLoop:
        if sum([toplist[2] == "X", midlist[1] == "X", bottomlist[0] == "X"]) == 2:
            if toplist[2] == "_":
                toplist[2] = "O"
                w.create_oval(100 * (3), 100, 100 * (4), 200)
                DefenseCheck = True

            elif midlist[1] == "_":
                midlist[1] = "O"
                w.create_oval(100 * (2), 200, 100 * (3), 300)
                DefenseCheck = True

            elif bottomlist[0] == "_":
                bottomlist[0] = "O"
                w.create_oval(100 * (1), 300, 100 * (2), 400)
                DefenseCheck = True

    return
################################################################################################
def WinComputer():
    global var
    global player1Loop
    global win
    global draw
    global TwoP
    player1Loop = True
    win = False

    if toplist.count("O") == 3 or midlist.count("O") == 3 or bottomlist.count("O") == 3:
        choose.set("COMPUTER WINS - Please choose an option")
        win = True
    elif toplist[0] == "O" and midlist[0] == "O" and bottomlist[0] == "O":
        choose.set("COMPUTER WINS - Please choose an option")
        win = True
    elif toplist[1] == "O" and midlist[1] == "O" and bottomlist[1] == "O":
        choose.set("COMPUTER WINS - Please choose an option")
        win = True
    elif toplist[2] == "O" and midlist[2] == "O" and bottomlist[2] == "O":
        choose.set("COMPUTER WINS - Please choose an option")
        win = True
    elif toplist[0] == "O" and midlist[1] == "O" and bottomlist[2] == "O":
        choose.set("COMPUTER WINS - Please choose an option")
        win = True
    elif toplist[2] == "O" and midlist[1] == "O" and bottomlist[0] == "O":
        choose.set("COMPUTER WINS - Please choose an option")
        win = True
    elif toplist.count("_") + midlist.count("_") + bottomlist.count("_") == 0:
        choose.set("GAME IS A DRAW")
        draw = True
    else:
        choose.set("It is your turn to move")

    if win or draw:
        w.create_rectangle(50, 450, 150, 500, fill="green")
        w.create_rectangle(200, 450, 300, 500, fill="yellow")
        w.create_rectangle(350, 450, 450, 500, fill="red")
        w.create_rectangle(50, 525, 150, 575, fill="purple")
        w.create_text(55, 475, anchor=W, font="Purisa", text="Level 1")
        w.create_text(205, 475, anchor=W, font="Purisa", text="Level 2")
        w.create_text(355, 475, anchor=W, font="Purisa", text="Level 3")
        w.create_text(55, 550, anchor=W, font="Purisa", text="2 Player")
        var = "True"

    return
################################################################################################
def WinPlayer():
    global var
    global winP
    global draw
    global letter
    global TwoP
    winP = False

    if toplist.count(letter) == 3 or midlist.count(letter) == 3 or bottomlist.count(letter) == 3:
        choose.set("PLAYER "+ letter +" WINS - Please choose an option")
        winP = True
    elif toplist[0] == letter and midlist[0] == letter and bottomlist[0] == letter:
        choose.set("PLAYER "+ letter +" WINS - Please choose an option")
        winP = True
    elif toplist[1] == letter and midlist[1] == letter and bottomlist[1] == letter:
        choose.set("PLAYER "+ letter +" WINS - Please choose an option")
        winP = True
    elif toplist[2] == letter and midlist[2] == letter and bottomlist[2] == letter:
        choose.set("PLAYER "+ letter +" WINS - Please choose an option")
        winP = True
    elif toplist[0] == letter and midlist[1] == letter and bottomlist[2] == letter:
        choose.set("PLAYER "+ letter +" WINS - Please choose an option")
        winP = True
    elif toplist[2] == letter and midlist[1] == letter and bottomlist[0] == letter:
        choose.set("PLAYER "+ letter +" WINS - Please choose an option")
        winP = True
    elif toplist.count("_") + midlist.count("_") + bottomlist.count("_") == 0:
        choose.set("GAME IS A DRAW")
        draw = True
    if TwoP:
        if letter == "X":
            letter = "O"
        else:
            letter = "X"


    if winP or draw:
        w.create_rectangle(50, 450, 150, 500, fill="green")
        w.create_rectangle(200, 450, 300, 500, fill="yellow")
        w.create_rectangle(350, 450, 450, 500, fill="red")
        w.create_rectangle(50, 525, 150, 575, fill="purple")
        w.create_text(55, 475, anchor=W, font="Purisa", text="Level 1")
        w.create_text(205, 475, anchor=W, font="Purisa", text="Level 2")
        w.create_text(355, 475, anchor=W, font="Purisa", text="Level 3")
        w.create_text(55, 550, anchor=W, font="Purisa", text="2 Player")
        var = "True"

    return
################################################################################################
def leftClick(event):
    global toplist
    global midlist
    global bottomlist
    global winP
    global win
    global firstmove
    global var
    global cPlay
    global level
    global draw
    global letter
    global TwoP
    global second
    global skip
    global skipT

    if event.x < 300 and event.x > 200 and event.y > 525 and event.y < 575:
        master.destroy()

    elif (event.x < 300 and event.x > 200 and event.y > 450 and event.y < 500 and var == "True"):
        level = 2
        letter = "X"
        TwoP = False
    elif (event.x < 150 and event.x > 50 and event.y > 450 and event.y < 500 and var == "True"):
        level = 1
        letter = "X"
        TwoP = False
    elif (event.x < 450 and event.x > 350 and event.y > 450 and event.y < 500 and var == "True"):
        level = 3
        letter = "X"
        TwoP = False
    elif (event.x < 150 and event.x > 50 and event.y > 525 and event.y < 575 and var == "True"):
        level = 4
        letter = "X"
        TwoP = True

    if (event.x < 300 and event.x > 200 and event.y > 450 and event.y < 500 and var == "True") or \
            (event.x < 150 and event.x > 50 and event.y > 450 and event.y < 500 and var == "True") or \
            (event.x < 450 and event.x > 350 and event.y > 450 and event.y < 500 and var == "True") or \
            (event.x < 150 and event.x > 50 and event.y > 525 and event.y < 575 and var == "True"):
        toplist = ["_", "_", "_"]
        midlist = ["_", "_", "_"]
        bottomlist = ["_", "_", "_"]
        w.delete("all")
        w.create_rectangle(200, 525, 300, 575, fill="white")
        w.create_text(205, 550, anchor=W, font="Purisa", text="Exit")
        w.create_text(250, 50, font=("Calibri, 18"), text="TIC TAC TOE ... by Dulhan")

        w.create_line(100, 100, 100, 400, fill="blue")
        w.create_line(200, 100, 200, 400, fill="blue")
        w.create_line(300, 100, 300, 400, fill="blue")
        w.create_line(400, 100, 400, 400, fill="blue")

        w.create_line(100, 100, 400, 100, fill="blue")
        w.create_line(100, 200, 400, 200, fill="blue")
        w.create_line(100, 300, 400, 300, fill="blue")
        w.create_line(100, 400, 400, 400, fill="blue")
        var = "False"
        firstmove = True
        draw = False
        winP = False
        win = False
        second = True

        if level != 4:
            skip = w.create_rectangle(50, 450, 450, 500, fill = "Orange")
            skipT = w.create_text(75, 475, anchor=W, font="Purisa", text="Click here to go second or anywhere else to go first ")
            choose.set("It is your turn to move")

    elif level != 4 and second:

        if event.x < 400 and event.x > 100 and event.y > 450 and event.y < 500:
            if level == 1:
                ComputerLevel1()
            elif level == 2:
                ComputerLevel2()
            else:
                ComputerLevel3()
        w.delete(skip)
        w.delete(skipT)
        second = False

    elif var == "False":

        if event.x > 100 and event.x < 200 and event.y > 100 and event.y < 200 and toplist[0] == "_":
            if letter == "X":
                w.create_line(100, 100, 200, 200)
                w.create_line(200, 100, 100, 200)
            else:
                w.create_oval(100, 100, 200, 200)
            toplist[0] = letter
            cPlay = True

        elif event.x > 200 and event.x < 300 and event.y > 100 and event.y < 200 and toplist[1] == "_":
            if letter == "X":
                w.create_line(200, 100, 300, 200)
                w.create_line(300, 100, 200, 200)
            else:
                w.create_oval(200, 100, 300, 200)
            toplist[1] = letter
            cPlay = True

        elif event.x > 300 and event.x < 400 and event.y > 100 and event.y < 200 and toplist[2] == "_":
            if letter == "X":
                w.create_line(300, 100, 400, 200)
                w.create_line(400, 100, 300, 200)
            else:
                w.create_oval(300, 100, 400, 200)
            toplist[2] = letter
            cPlay = True

        elif event.x > 100 and event.x < 200 and event.y > 200 and event.y < 300 and midlist[0] == "_":
            if letter == "X":
                w.create_line(100, 200, 200, 300)
                w.create_line(200, 200, 100, 300)
            else:
                w.create_oval(100, 200, 200, 300)
            midlist[0] = letter
            cPlay = True

        elif event.x > 200 and event.x < 300 and event.y > 200 and event.y < 300 and midlist[1] == "_":
            if letter == "X":
                w.create_line(200, 200, 300, 300)
                w.create_line(300, 200, 200, 300)
            else:
                w.create_oval(200, 200, 300, 300)
            midlist[1] = letter
            cPlay = True

        elif event.x > 300 and event.x < 400 and event.y > 200 and event.y < 300 and midlist[2] == "_":
            if letter == "X":
                w.create_line(300, 200, 400, 300)
                w.create_line(400, 200, 300, 300)
            else:
                w.create_oval(300, 200, 400, 300)
            midlist[2] = letter
            cPlay = True

        elif event.x > 100 and event.x < 200 and event.y > 300 and event.y < 400 and bottomlist[0] == "_":
            if letter == "X":
                w.create_line(100, 300, 200, 400)
                w.create_line(200, 300, 100, 400)
            else:
                w.create_oval(100, 300, 200, 400)
            bottomlist[0] = letter
            cPlay = True

        elif event.x > 200 and event.x < 300 and event.y > 300 and event.y < 400 and bottomlist[1] == "_":
            if letter == "X":
                w.create_line(200, 300, 300, 400)
                w.create_line(300, 300, 200, 400)
            else:
                w.create_oval(200, 300, 300, 400)
            bottomlist[1] = letter
            cPlay = True

        elif event.x > 300 and event.x < 400 and event.y > 300 and event.y < 400 and bottomlist[2] == "_":
            if letter == "X":
                w.create_line(300, 300, 400, 400)
                w.create_line(400, 300, 300, 400)
            else:
                w.create_oval(300, 300, 400, 400)
            bottomlist[2] = letter
            cPlay = True

        else:
            cPlay = False


        WinPlayer()
        if cPlay:
            if (not winP and not win and not draw) and level == 1:
                if toplist.count("_") + midlist.count("_") + bottomlist.count("_") > 0:
                    ComputerLevel1()
            elif (not winP and not win and not draw) and level == 2:
                if toplist.count("_") + midlist.count("_") + bottomlist.count("_") > 0:
                    ComputerLevel2()
            elif (not winP and not win and not draw) and level == 3:
                if toplist.count("_") + midlist.count("_") + bottomlist.count("_") > 0:
                    ComputerLevel3()
            elif (not winP and not win and not draw) and level == 4:
                if toplist.count("_") + midlist.count("_") + bottomlist.count("_") > 0:
                    choose.set("Player " + letter + " Move")


            cPlay = False
        else:
            choose.set("Please choose a square that is not filled")
    return
################################################################################################
def ComputerLevel1():
    choose.set("")
    player2Loop = True

    while player2Loop:
        if toplist.count("_") + midlist.count("_") + bottomlist.count("_") > 0:
            row = random.randint(1, 3)
            col = random.randint(1, 3)

            if row == 1 and toplist[col - 1] == "_":
                toplist[col - 1] = "O"
                w.create_oval(100 * col, 100, 100 * (col + 1), 200)
                break
            elif row == 2 and midlist[col - 1] == "_":
                midlist[col - 1] = "O"
                w.create_oval(100 * col, 200, 100 * (col + 1), 300)
                break
            elif row == 3 and bottomlist[col - 1] == "_":
                bottomlist[col - 1] = "O"
                w.create_oval(100 * col, 300, 100 * (col + 1), 400)
                break
            else:
                player2Loop = True
        else:
            choose.set("Game is done")

    WinComputer()

    return
################################################################################################
def ComputerLevel2():
    choose.set("")
    player2Loop = True
    Defense()
    while player2Loop:
        if not DefenseCheck:
            row = random.randint(1, 3)
            col = random.randint(1, 3)

            if row == 1 and toplist[col - 1] == "_":
                toplist[col - 1] = "O"
                w.create_oval(100 * col, 100, 100 * (col + 1), 200)
                break
            elif row == 2 and midlist[col - 1] == "_":
                midlist[col - 1] = "O"
                w.create_oval(100 * col, 200, 100 * (col + 1), 300)
                break
            elif row == 3 and bottomlist[col - 1] == "_":
                bottomlist[col - 1] = "O"
                w.create_oval(100 * col, 300, 100 * (col + 1), 400)
                break
            else:
                player2Loop = True
        else:
            break

    WinComputer()

    return
################################################################################################
def ComputerLevel3():
    global firstmove
    global DefenseCheck
    choose.set("")
    player2Loop = True
    if firstmove and midlist[1] == "_":
        w.create_oval(200, 200, 300, 300)
        midlist[1] = "O"
        firstmove = False
    elif ((midlist[1] == "O" and toplist[0] == "X" and bottomlist[2] == "X") or (
                midlist[1] == "O" and toplist[2] == "X" and bottomlist[0] == "X")) and toplist.count(
            "_") + midlist.count("_") + bottomlist.count("_") == 6:
        guess = random.randint(1, 4)
        if guess == 1:
            w.create_oval(100, 200, 200, 300)
            midlist[0] = "O"
        elif guess == 2:
            w.create_oval(300, 200, 400, 300)
            midlist[2] = "O"
        elif guess == 3:
            w.create_oval(200, 300, 300, 400)
            bottomlist[1] = "O"
        elif guess == 4:
            w.create_oval(200, 100, 300, 200)
            toplist[1] = "O"
    else:
        Offense()
        if not OffenseCheck:
            Defense()
        while player2Loop:
            if not DefenseCheck and not OffenseCheck:
                row = random.randint(1, 3)
                col = random.randint(1, 3)

                if row == 1 and toplist[col - 1] == "_":
                    toplist[col - 1] = "O"
                    w.create_oval(100 * col, 100, 100 * (col + 1), 200)
                    break
                elif row == 2 and midlist[col - 1] == "_":
                    midlist[col - 1] = "O"
                    w.create_oval(100 * col, 200, 100 * (col + 1), 300)
                    break
                elif row == 3 and bottomlist[col - 1] == "_":
                    bottomlist[col - 1] = "O"
                    w.create_oval(100 * col, 300, 100 * (col + 1), 400)
                    break
                else:
                    player2Loop = True
            else:
                break

        WinComputer()

    return
################################################################################################

w = Canvas(master, width=500, height=600, bg="grey", highlightbackground="blue")
w.title = "Tic Tac Toe... by Dulhan Naidappuwa Waduge"

w.create_line(100, 100, 100, 400, fill = "blue")
w.create_line(200, 100, 200, 400, fill = "blue")
w.create_line(300, 100, 300, 400, fill = "blue")
w.create_line(400, 100, 400, 400, fill = "blue")

w.create_line(100, 100, 400, 100, fill = "blue")
w.create_line(100, 200, 400, 200, fill = "blue")
w.create_line(100, 300, 400, 300, fill = "blue")
w.create_line(100, 400, 400, 400, fill = "blue")

w.create_rectangle(50, 450, 150, 500, fill="green")
w.create_rectangle(200, 450, 300, 500, fill="yellow")
w.create_rectangle(350, 450, 450, 500, fill="red")
w.create_rectangle(200, 525, 300, 575, fill="white")
w.create_rectangle(50, 525, 150, 575, fill="purple")
w.create_text(55, 475, anchor=W, font="Purisa", text="Level 1")
w.create_text(205, 475, anchor=W, font="Purisa", text="Level 2")
w.create_text(355, 475, anchor=W, font="Purisa", text="Level 3")
w.create_text(205, 550, anchor=W, font="Purisa", text="Exit")
w.create_text(55, 550, anchor=W, font="Purisa", text="2 Player")
w.create_text(250, 50, font = ("Calibri, 18"), text = "TIC TAC TOE ... by Dulhan")

choose = StringVar()
choose.set("Please choose an option")

L1 = Label(master, textvariable=choose)
L1.pack(side=BOTTOM)

master.bind("<Button-1>", leftClick)
w.pack(side=LEFT)
master.mainloop()
