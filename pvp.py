import RequiredFunctions as rf





def play_game():
    board=[' ' for i in range(9)]

    symbol='X'

    while True:
        rf.print_board(board)
        
        if(symbol=='X'):
            print("Player1 : Your Symbol 'X'")
            rf.take_input(board,symbol)

            if(rf.check_win(board,symbol)):
                rf.print_board(board)
                print("----------------------------------------Conguralation----------------------------------------\nPlayer1(X) Wins!!\n\n\n")
                break

            else:
                if(rf.check_draw(board)):
                    print("<!><!>Draw!!\n<!><!>No One Win!!\n\n\n")
                    break
            

        else:
            print("Player2 : Your Symbol 'O'")
            rf.take_input(board,symbol)

            if(rf.check_win(board,symbol)):
                rf.print_board(board)
                print("----------------------------------------Conguralation---------------------------------\nPlayer2(O) Wins!!\n\n\n")
                break

            else:
                if(rf.check_draw(board)):
                    print("<!><!>Draw!!\n<!><!>No One Win!!\n\n\n")
                    break

        if(symbol=='X'):
            symbol='O'
        else:
            symbol='X'
