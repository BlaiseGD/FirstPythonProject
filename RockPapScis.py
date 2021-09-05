from random import randrange
reset = 'y'
while reset == 'y':
    print("This is rock, paper, scissors against a computer!\ny means yes and n means no\nEnter 1 for rock, 2 for paper, or 3 for scissors")
    #1 is rock 2 is paper 3 is scissors for compInput
    computerInput = randrange(1, 4)
    userInput = int(input())
    if(userInput == 1 and computerInput == 3):
        print("\n\nYou Win\n!")
    elif(userInput == 2 and computerInput == 1):
        print("\n\nYou Win!\n")
    elif(userInput == 3 and computerInput == 2):
        print("\n\nYou Win!\n")
    elif(userInput == computerInput):
        print("\n\nYou tied\n")
    else:
        print("\n\nYou lose!\n")
    print("Your input was " + str(userInput) +"\nThe computer input was " + str(computerInput) + "\nDo you want to play again\n")
    reset = input()


#The commented code is the original and is much cleaner to play
#The uncommented code is the shortest I could get it with it retaining full functionality

#from random import randrange
#import os
#clear = lambda: os.system('clear');
#reset = 'y';
#while reset == 'y':
    #print("This is rock, paper, scissors against a computer!")
    #print("y means yes and n means no");
    #print("Enter 1 for rock, 2 for paper, or 3 for scissors")
    #1 is rock 2 is paper 3 is scissors for compInput
    #computerInput = randrange(1, 4);
    #userInput = int(input());
    #if(userInput == 1 and computerInput == 3):
    #    clear();
    #    print("You Win!");
    #elif(userInput == 2 and computerInput == 1):
    #    clear();
    #    print("You Win!");
    #elif(userInput == 3 and computerInput == 2):
    #    clear();
    #    print("You Win!")
    #elif(userInput == computerInput):
    #    print("You tied");
    #else:
    #    print("You lose!")
    #print("Your input was " + str(userInput))
    #print("The computer input was " + str(computerInput))
    #print("Do you want to play again?");
    #reset = input();
    #clear();

