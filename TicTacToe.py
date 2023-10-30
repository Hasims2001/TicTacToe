import random

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
userScore = computerScore = 0
winner = ""
def UpdateBoard():
    global board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def UpdateView():
    global board
    global winner
    print(f"----------------{winner}---------------\n|    {board[0][0]}    |    {board[0][1]}    |    {board[0][2]}    |\n|    {board[1][0]}    |    {board[1][1]}    |    {board[1][2]}    |\n|    {board[2][0]}    |    {board[2][1]}    |    {board[2][2]}    |\n-------------------------------\n")

  

def Instruction():
    print("\nWelcome to Tic Tac Toe Game")
    print("\nHere are some Instruction to play game:")
    print("\n-> You have to enter your move with row and column wisely.\nfor example in 3X3 board: A1(Top left), B2(center) C3(bottom right)")
Instruction()

def GetInput(msg, options):
    try:
        val = int(input(msg))
        if(val in options):
            return val
        else:
            print("please choose correct option")
            GetInput(msg, options)
    except:
        print("please enter number.")
        GetInput(msg, options)

def OnePlayerWinner(val):
    if(val == -1):
        print("-*-*-*-*-*-It's Draw!-*-*-*-*-*-")
    elif(val == "X"):
        print("-*-*-*-*-*-You are Winner-*-*-*-*-*-")
    else:
        print("-*-*-*-*-*-Computer is Winner-*-*-*-*-*-")

def TwoPlayerWinner(val):
    if(val == -1):
        print("-*-*-*-*-*-It's Draw!-*-*-*-*-*-")
    elif(val == "X"):
        print("-*-*-*-*-*-Player 1 is Winner-*-*-*-*-*-")
    else:
        print("-*-*-*-*-*-Player 2 is Winner-*-*-*-*-*-")


def UserMove(msg, val):
    try:
        global board
        move = [*input(msg)] 
        col = int(move[1])-1
        if(col < 0 or col > 3):
            print("invalid position")
            UserMove(msg, val)
        else:
            row = None
            if(move[0] == 'A'):
                row = 0
            elif(move[0] == 'B'):
                row = 1
            elif(move[0] == 'C'):
                row = 2

            if((board[row][col] == " ") or (board[row][col] == " ") or (board[row][col] == " ")):
                board[row][col] = val
                check = CheckWinner()
                if(check != 0):
                    TwoPlayerWinner(check) 
                    return 1 
                elif( check == -1):
                    TwoPlayerWinner(check)
                    return 1                  
            else:
                check = CheckWinner()
                if(check == 0):
                    print("place is already registerd or invalid position")
                    UserMove(msg, val)
                elif( check == -1):
                    TwoPlayerWinner(check)
                    return 1
            return 0

    except:
        print("please choose correct move")
        UserMove(msg, val)

def ComputerMove():
    global board
    available = [(i, j) for i in range(3) for j in range(3) if(board[i][j] == " ")]
    if(available):
        row, col = random.choice(available)
        print("computer move")
        board[row][col] = "O"
        check = CheckWinner()
        if(check != 0):
            OnePlayerWinner(check) 
            return 1
        return 0
    else:
        return("The board is full, It's draw!")

def CheckWinner():
    global board
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    if (board[0][0] == board[1][1] == board[2][2] or
        board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
        return board[1][1]

    available = [(i, j) for i in range(3) for j in range(3) if(board[i][j] == " ")]
    if(not available):
        return -1
    return 0


def OnePlayer():
    global board
    UpdateView()
    checkedOne = UserMove("your move:", "X")
    UpdateView()
    if(checkedOne == 0):
        checkedTwo = ComputerMove()
        UpdateView()
        if(checkedTwo == 0):
            OnePlayer()


def TwoPlayer():
    global board
    UpdateView()
    checkedOne = UserMove("Player 1 move:", "X")
    UpdateView()
    if(checkedOne == 0):
        checkedTwo = UserMove("Player 2 move:", "O")
        UpdateView()
        if(checkedTwo == 0):
            TwoPlayer()


def GameMenu():
    print("\n----------Tic Tac Toe----------")
    print("|        1. One Player       |")
    print("|        2. Two Player       |")
    print("|        3. Custom Layout    |")
    print("|        4. Exit             |")
    print("--------------------------------")
    option = GetInput("Choose one option:", [1,2,3,4])
    
    if(option == 1):
        UpdateBoard()
        OnePlayer()
        GameMenu()
    elif(option == 2):
        UpdateBoard()
        TwoPlayer()
        GameMenu()
    elif(option == 3):
        print("Feature is under development, sorry for inconvenience")
        GameMenu()
    elif(option == 4):
        print("Good Bye...")

GameMenu()