board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

gamestillgoing=True
winner=None

currentplayer="X"


def displayboard():
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(board[8] + " | " + board[7] + " | " + board[6] + " | ")


def playgame():
    # Display Initial Board
    displayboard()

    while gamestillgoing:

      handleturn(currentplayer)

      checkifgameover()

      flipplayer()

    if winner=="X" or winner=="O":
          print(winner+" Won.")

    elif winner==None:
     print("Tie")




def handleturn(player):
    print(player+"'s Turn.")
    position = input("Choose a position from 1-9: ")

    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position=input("Invalid Input.")
    position = int(position) - 1

    if board[position]!="-":
        print("You cant go there a  again")
    board[position] = player
    displayboard()

def checkifgameover():
    checkforwinner()
    checkiftie()


def checkforwinner():
    global winner


    rowwinner=checkrows()
    columnwinner=checkcolumns()
    diagnolwinner=checkdiagnols()

    if rowwinner:
       winner=rowwinner

    elif columnwinner:
        winner = columnwinner



    elif diagnolwinner:
        winner=diagnolwinner

    else:
        winner=None

    return

def checkrows():
    global gamestillgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gamestillgoing=False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkcolumns():
    global gamestillgoing
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        gamestillgoing = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

    return

def checkdiagnols():
    global gamestillgoing
    diagonals1 = board[0] == board[4] == board[6] != "-"
    diagonals2 = board[6] == board[4] == board[2] != "-"
    "-"

    if diagonals1 or diagonals2:
        gamestillgoing = False

    if diagonals1:
        return board[0]
    elif diagonals2:
        return board[1]

    return

def checkiftie():
    global gamestillgoing
    if "-" not in board:
        gamestillgoing=False
    return


def flipplayer():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    elif currentplayer=="O":
        currentplayer="X"
    return


playgame()

#board
#display board
#play game
#handle turn
#check win
#check rows
#check diagnols
#check tie
#flip player

