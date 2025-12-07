def printboard(board):
    for row in board:
        print("|".join(row))
    print("." * 5)

def checkwinner(board,player):
    for row in board: #Check rows
        if all(cell==player for cell in board):
            return True   
    for col in range(3): 
        if all(board[row][col]==player for row in range(3)): #Check Columns
            return True
        if all(board[i][i]==player for i in range(3)): #Check Diagonals
            return True
        if all(board[i][2-i]==player for i in range(3)):
            return True
    return False

def isboardfull(board): #Check if the board is full
    for row in board:
        for cell in row:
            if cell=="":
                return False
    return True

def main():
    board=[["" for _ in range(3)]for _ in range(3)]
    players=["X","O"] #Define the players
    turn =0

    print("Welcome to TIC TAC TOE")
    printboard(board)

    while(True):
        player=players[turn%2] #This alternates the turns between the players
        print(f"player{player}'s Turn")
        row=int(input("Enter the row 0,1,2:"))
        col=int(input("Enter the column 0,1,2:"))
        if board[row][col]=="": #If the cell is empty, the player's move is placed there
            board[row][col]=player
            printboard(board)
            if checkwinner(board,player):
                print(f"Player {player} wins")
                break
            elif isboardfull(board):
                print("Draw")
                break
            turn+=1
        else:
            print("That cell is occupied . Try different cell")
if __name__=="__main__":
    main()
