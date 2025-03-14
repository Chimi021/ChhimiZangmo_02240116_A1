#ASSIGNMENT PART B (Games)
print("WELCOME TO THE GAME CENTER!! ;) ")
print("Choose the game you would like to play(1 or 2)")
def Menu():
    print("1) Number Guessing Game.")
    print("2) Rock, Paper, Scissors.")
    print("3) Exit.")
# Menu()

def Num_guess():
    import random
    Mystery_num = random.randint(1, 100)
    Attempts = 0
    max_attempts = 5
    print("WELCOME TO THE MYSTERY NUMBER GAME!! ^u^")
    print("You have 5 attempts to guess the mystery number.")
    print("The Mystery number is between 1 and 100.")
    while Attempts < max_attempts: 
        Attempts += 1
        user = int(input("Enter your guess: "))
        if user == Mystery_num:
            print("Congratulations! You found the mystery number.")
            break
        elif user > Mystery_num:
            print("Your guess is higher then the mystery number.")
        elif user < Mystery_num:
            print("Your guess is lower then the mystery number.")
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
    else:  
        print ("YOU LOST! T_T .. You reached maximum attempts.")
        print("The Mystery number was", Mystery_num)
# Num_guess()

def RPS ():
    import random
    print("WELCOME HUMAN!")
    print("I am your opponent, the computer.")
    print("Let's play Rock(R), Paper(P), or Scissors(S) !")
    rps = random.choice(['Rock','Paper','Scissors'])
    u = input("Display your weapon : ") 
    if u == "R" and rps == "Rock" or  u == "P" and rps == "Paper"  or u == "S" and rps == "Scissors":
        print("My weapon is", rps)
        print("It's a tie!")
    elif u == "R" and rps == "Paper":
        print("My weapon is", rps)
        print("You lose T_T")
    elif u == "R" and rps == "Scissors":
        print("My weapon is", rps)
        print("You win!^u^")
    elif u == "P" and rps == "Rock":
        print("My weapon is", rps)
        print("You win! ^u^")
    else:
        print("Invalid input. Try R, P or S.")
# RPS ()

while True:
    Menu()
    c = input("What would you like to do? Enter a number(1-3):")
    if c == '1':
        Num_guess()
    elif c == '2':
        RPS()
    elif c == '3':
        print("Thank you for visiting. ^U^")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 3.")

    Again = input("Would you like to play again? (Y/N): ")
    if Again == 'Y':
        continue
    elif Again == 'N':
        print("Bye bye, Thank you for visiting. ^U^")
        break
    else:
        print("Invalid input. Please enter Y or N.")
        break