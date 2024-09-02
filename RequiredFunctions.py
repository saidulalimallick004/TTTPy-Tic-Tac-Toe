import random

def print_board(board):
    print(f"\n \t\t\t\t {board[0]} | {board[1]} | {board[2]}")
    print("\t\t\t\t---+---+---")
    print(f" \t\t\t\t {board[3]} | {board[4]} | {board[5]}")
    print("\t\t\t\t---+---+---")
    print(f" \t\t\t\t {board[6]} | {board[7]} | {board[8]}")



def take_input(board,symbol):
    while True:
        print("Enter Choice (1-9): ")
        while True:
            try:
                place=int(input("  >>"))
                break
            except:
                print("Enter A valid Empty Space(1-9):")
                
        if(place<=0 or place>9):
            print("\n\n<!><!>Invalid Choice!!\n<!><!>Try again!!")
            print_board(board)
            
        elif(board[place-1]==' '):
            board[place-1]=symbol
            break
        elif(board[place-1]!=' '):
            print("\n\n<!><!>Already Ocuppied\n<!><!>Try again!!")
            print_board(board)

        else:
            continue


def com_input(board,symbol):

    left_place=[]
    for i in range(len(board)):
        if board[i]==' ':
            left_place.append(i)

    random_place=random.choice(left_place)
    board[random_place]=symbol



def check_win(board,symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]               
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

        

def check_draw(board):
    a=0
    for i in board:
        if(i!=' '):
            a+=1

    if(a==9):
        return True
    else:
        return False
    
    
