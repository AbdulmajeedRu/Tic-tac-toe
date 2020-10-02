player1 = [0,0,0,0,0,0,0,0,0]
player2 = [0,0,0,0,0,0,0,0,0]
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

turn = 1

def boardp():
    ibrahim = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = ibrahim
            ibrahim = ibrahim + 1
    print("  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], " ")
    print("  ____________________")
    print("  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], " ")
    print("  ____________________")
    print("  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], " ")

def play(turn=turn):

    boardp()

    if turn == 1:
        p = int(input("Player 1 turn, choose an area to play:"))
        for i in range(3):
            for j in range(3):
                if p == board[i][j]:
                    board[i][j] = 1
        player1[p-1] = 1
        turn = 2
        check(p)
    else:
        p = int(input("Player 2 turn, choose an area to play:"))
        for i in range(3):
            for j in range(3):
                if p == board[i][j]:
                    board[i][j] = 2
        player2[p-1] = 1
        turn = 1
        check(p)


def check(p):
    if board[0][0] == 1 & board[0][1] == 1 & board[0][2] == 1:
        print("Player 1 wins.")
        exit(0)
    elif board[1][0] == 1 & board[1][1] == 1 & board[1][2] == 1:
        print("Player 1 wins.")
        exit(0)
    elif board[2][0] == 1 & board[2][1] == 1 & board[2][2] == 1:
        print("Player 1 wins.")
        exit(0)
    elif (board[0][0] == 1 & board[1][0] == 1 & board[2][0] == 1):
        print("Player 1 wins.222")
        exit(0)
    elif board[0][1] == 1 & board[1][1] == 1 & board[2][1] == 1:
        print("Player 1 wins.")
        exit(0)
    elif board[0][2] == 1 & board[1][2] == 1 & board[1][3] == 1:
        print("Player 1 wins.")
        exit(0)
    elif (board[0][0] == 1) & (board[1][1] == 1) & (board[2][2] == 1):
        print("Player 1 wins.111")
        exit(0)
    elif board[0][2] == 1 & board[1][1] == 1 & board[2][0] == 1:
        print("Player 1 wins.")
        exit(0)
    elif board[0][0] == 2 & board[0][1] == 2 & board[0][2] == 2:
            print("Player 2 wins.")
            exit(0)
    elif board[1][0] == 2 & board[1][1] == 2 & board[1][2] == 2:
            print("Player 2 wins.")
            exit(0)
    elif board[2][0] == 2 & board[2][1] == 2 & board[2][2] == 2:
            print("Player 2 wins.")
            exit(0)
    elif board[0][0] == 2 & board[1][0] == 2 & board[2][0] == 2:
            print("Player 2 wins.")
            exit(0)
    elif board[0][1] == 2 & board[1][1] == 2 & board[2][1] == 2:
            print("Player 2 wins.")
            exit(0)
    elif (board[0][2] == 2 & board[1][2] == 2 & board[1][3] == 2):
            print("Player 2 wins.")
            exit(0)
    elif board[0][0] == 2 & board[1][1] == 2 & board[2][2] == 2:
            print("Player 2 wins.")
            exit(0)
    elif (board[0][2] == 2 & board[1][1] == 2 & board[2][0] == 2):
            print("Player 2 wins.")
            exit(0)
    else:
        play()


print("This is an XO game made using python.\nFirst player will be X, Second player will be O"
      " \nGame board will be numbered from 1 to 9, each player will take a turn to choose their selected square.")

while(1):
    play()