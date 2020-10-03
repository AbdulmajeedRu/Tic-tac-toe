board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
checklist =[]

turn = 1
counter = 0

def restart():
    global board
    global checklist
    global turn
    global counter
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    checklist = []

    turn = 1
    counter = 0


def boardp():

    print("  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], " ")
    print("  ____________________")
    print("  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], " ")
    print("  ____________________")
    print("  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], " ")
    print("")

def play():
    global turn
    global counter
    global checklist
    boardp()


    if turn == 1:
        try:
            p = int(input("Player 1 turn, choose an area to play:"))
            print("")
        except:
            print("That's not a valid option, please input an integer.")
            pass
            play()


        if p in checklist:
            print("Area is already taken, choose a different one.")
            play()
        for i in range(3):
            for j in range(3):

                if p == board[i][j]:
                    board[i][j] = 'X'
                    checklist.append(p)


        turn = 2
        counter = counter + 1
        check(p)

    else:
        try:
            p = int(input("Player 2 turn, choose an area to play:"))
            print("")
        except:
            print("That's not a valid option, please input an integer.")
            pass
            play()
        if p in checklist:
            print("Area is already taken, choose a different one.")
            play()
        for i in range(3):
            for j in range(3):
                if p == board[i][j]:
                    board[i][j] = 'O'
                    checklist.append(p)


        turn = 1
        counter = counter + 1
        check(p)


def check(p):
    global counter
    for i in range(8):
        for j in range(3):
            if (board[j][0] == 'X') & (board[j][1] == 'X') & (board[j][2] == 'X'):
                boardp()
                print("Player 1 wins.")
                exit(0)
            elif (board[0][j] == 'X') & (board[1][j] == 'X') & (board[2][j] == 'X'):
                boardp()
                print("Player 1 wins.")
                exit(0)
            elif (board[0][0] == 'X') & (board[1][1] == 'X') & (board[2][2] == 'X'):
                boardp()
                print("Player 1 wins.")
                exit(0)
            elif (board[0][2] == 'X') & (board[1][1] == 'X') & (board[2][0] == 'X'):
                boardp()
                print("Player 1 wins.")
                exit(0)
            elif (board[j][0] == 'O') & (board[j][1] == 'O') & (board[j][2] == 'O'):
                boardp()
                print("Player 2 wins.")
                exit(0)
            elif (board[0][j] == 'O') & (board[1][j] == 'O') & (board[2][j] == 'O'):
                boardp()
                print("Player 2 wins.")
                exit(0)
            elif (board[0][0] == 'O') & (board[1][1] == 'O') & (board[2][2] == 'O'):
                boardp()
                print("Player 2 wins.")
                exit(0)
            elif (board[0][2] == 'O') & (board[1][1] == 'O') & (board[2][0] == 'O'):
                boardp()
                print("Player 2 wins.")
                exit(0)
            else:
                if counter >= 9:
                    boardp()
                    print("Result is draw, finishing game.")
                    exit(0)
                continue




print("This is a Tic Tac Toe game made using python.\nFirst player will be X, Second player will be O"
      " \nGame board will be numbered from 1 to 9, each player will take a turn to choose their selected square.")

for i in range(8):
    play()

x = input("\n Enter 1 to play again, anything else to stop playing.")
if (x == '1'):
    restart()
    for i in range(8):
        play()
else:
    exit(0)