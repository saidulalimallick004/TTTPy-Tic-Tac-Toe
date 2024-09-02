import pvp
import pvc

print("\n\n\nWelcome-------------------------------")

while True:
    print("1 | Player VS Player\n2 | Player VS Computer\n3 | Player VS AI\n4 | Exit")
    
    while True:
        try:
            choice=int(input("   >>"))
            break
        except:
            print("\n\n<!><!>Error\n<!><!>Enter Between 1-9: A Numeric Value")

    if(choice==1):
        print("Game Mode: Player VS Player------------------------------------------------------------------------------")
        pvp.play_game()
        
    elif(choice==2):
        print("Game Mode: Player VS Computer------------------------------------------------------------------------------")

        pvc.play_game()

    elif(choice==3):
        print("Comming Soon!!")

    elif(choice==4):
        print("Bye Bye!!\n")
        break

    else:
        print("<!><!>Invalid Choice!!\n<!><!>Try again!!")



print("---------------End-------------")