#Climb to the mountain game
#Author: LE Nguyen Thanh Toan
#Email: acemarco9@gmail.com

import random

die1 = 0                                    #initialize the variable for die1 and die2
die2 = 0                   
target = 1                                      #initialize the target to 1
go_on = ""
user_total = 0                                  #count how many times user rolled in their turn
computer_total = 0                              #count how many times computer rolled in its turn
play_again = "y"                               #for user to decide if they want another game
high_total = -1
low_total = -1
while play_again == "y" :
    choose_first = input("Do you want to roll first (y | n):")
    while choose_first != "y" and choose_first != "n" :                 #force user to enter "y" or "n", if user type anything else, type again
        print("Error: Please only enter 'y' or 'n'....")
        choose_first = input("Do you want to roll first (y | n):")
    print("\n")
    if choose_first == "y" :                    #user enter "y" it means the first turn is user's turn and the second turn is computer's turn
        while target < 7 and go_on == "" and die1 != target and die2 != target and die1+die2 != target :   #the loop will do until target=7,  it means the loop will do 6 times until it stop
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("You rolled a", die1, "and a", die2)
            user_total += 1
            if die1 == target or die2 == target :
                print("One dice match the target", str(target)+"!" )
                target += 1
                go_on = input("Press enter to continue")  #update go_on which allow user to decide if they want to continue or not
                while go_on != "" :
                    print("You need to press enter to finish your turn: ")
                    go_on = input("Press enter to continue")
                print("\n")
            elif die1+die2 == target :
                print("The sum of dice match the target", str(target)+"!")
                target += 1
                go_on = input("Press enter to continue")
                while go_on != "" :
                    print("You need to press enter to finish your turn: ")
                    go_on = input("Press enter to continue")
                print("\n")
            die1 = 0         #reset die1 and die2 to make sure the dice of previous target will not affect on the current target in the while loop
            die2 = 0
        target = 1          #reset target, because after a turn, target now is 7, reset target for the next turn
        while target < 7 and die1 != target and die2 != target and die1+die2 != target :   #the loop will do until target=7, it means the loop will do 6 times until it stop
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("The computer rolled a", die1, "and a", die2)
            computer_total += 1
            if die1 == target or die2 == target :
                print("One dice match the target", str(target)+"!" )
                target += 1
                print("\n")
            elif die1+die2 == target :
                print("The sum of dice match the target", str(target)+"!")
                target += 1
            die1 = 0         #reset die1 and die2 to make sure the dice of previous target will not affect on the current target in the while loop
            die2 = 0
        target = 1          ##target now is 7, we need to reset target for the next game
    elif choose_first == "n" :                                  #user enter "n" it means the first turn is computer's turn and the second turn is user's turn
        while target < 7 and die1 != target and die2 != target and die1+die2 != target :   #the loop will do until target=7, it means the loop will do 6 times until it stop
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("The computer rolled a", die1, "and a", die2)
            computer_total += 1
            if die1 == target or die2 == target :
                print("One dice match the target", str(target)+"!" )
                target += 1
                print("\n")
            elif die1+die2 == target :
                print("The sum of dice match the target", str(target)+"!")
                target += 1
                print("\n")
            die1 = 0         #reset die1 and die2 to make sure the dice of previous target will not affect on the current target in the while loop
            die2 = 0
        target = 1          ##reset target, because after a turn, target now is 7, reset target for the next turn
        while target < 7 and go_on == "" and die1 != target and die2 != target and die1+die2 != target :   #the loop will do until target=7,  it means the loop will do 6 times until it stop
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("You rolled a", die1, "and a", die2)
            user_total += 1
            if die1 == target or die2 == target :
                print("One dice match the target", str(target)+"!" )
                target += 1
                go_on = input("Press enter to continue")        #update go_on which allow user to decide if they want to continue or not
                while go_on != "" :
                    print("You need to press enter to finish your turn: ")
                    go_on = input("Press enter to continue")
                print("\n")
            elif die1+die2 == target :
                print("The sum of dice match the target", str(target)+"!")
                target += 1
                go_on = input("Press enter to continue")
                while go_on != "" :
                    print("You need to press enter to finish your turn: ")
                    go_on = input("Press enter to continue")
                print("\n")
            die1 = 0         #reset die1 and die2 to make sure the dice of previous target will not affect on the current target in the while loop
            die2 = 0
        target = 1          #target now is 7, we need to reset target for the next game
        print("\n")

    print("Game Statistic ... ")
    print("\n")
    average_roll = (user_total + computer_total) / 2
    average_per_target = average_roll / 6
    print("|", format("Player", "^10s"), "|", format("Computer", "^10s"),"|", format("Average", "^11s"),"|", format("Avg/Target", "^12s"), end="| \n")
    for i in range(55):
       print('-', end='')
    print("")
    print("|", format(user_total, "^10d"),"|", format(computer_total, "^10d"),"|", format(average_roll, "^11.2f"),"|", format(average_per_target, "^12.2f"), end="| \n"  )

    if high_total == -1 and low_total == -1 and user_total > computer_total :       #for the first game
        high_total = user_total
        low_total = computer_total
    elif high_total == -1 and low_total == -1 and user_total < computer_total :     #for the first game
        high_total = computer_total
        low_total = user_total
    elif user_total > high_total and user_total > computer_total and computer_total < low_total :   #user roll is global max and computer roll is global min
        high_total = user_total
        low_total = computer_total
    elif computer_total > high_total and computer_total > user_total and user_total < low_total :   #users roll is global min and computer roll is global max
        high_total = computer_total
        low_total = user_total
    elif user_total > high_total and user_total > computer_total :                                  #just user roll is global max, computer roll is not global max or global min
        high_total = user_total
    elif computer_total > high_total and computer_total > user_total :                              #just computer roll is global max, user roll is not global max or global min
        high_total = computer_total
    elif user_total < low_total and user_total < computer_total :                                   #just user roll is global min, computer rolls is not global max or global min
        low_total = user_total
    elif computer_total < low_total and computer_total < user_total :                               #just computer rolls is global min, user rolls is not global max or global min
        low_total = computer_total
    
    print("")   
    print("Global statistics ... ")
    print("")
    print("|", format("Max Total", "^11s"), "|", format("Min Total", "^11s"), "|" )
    for i in range(29):
       print('-', end='')
    print("")
    print("|", format(high_total, "^11d"), "|", format(low_total, "^11d"), "|" )
    
    user_total = 0                                      #reset user_total and computer_total for each game
    computer_total = 0
    

    play_again = input("Would you want to play again (y | n)? ")
    while play_again != "y" and play_again != "n" :             
        print("Error: Please only enter 'y' or 'n'")
        play_again = input("Would you want to play again (y | n)? ")
        

    


    
                

