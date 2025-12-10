import random

guess = ['rock','scissor','paper']
while True:
    computer_guess= random.choice(guess)

    user_guess=input("Enter your choice (Rock, Scissor or Paper):").lower()

    if computer_guess == user_guess :
        print("Its tie !!")
        print("Computer = ",computer_guess," You = ",user_guess)
    elif computer_guess == 'rock' and user_guess == 'paper' or \
        computer_guess == 'scissor' and user_guess == 'rock' or \
        computer_guess == 'paper' and user_guess == 'scissor' :
            print("You won!!👌")
            print("Computer = ",computer_guess," You = ",user_guess)
            choice=input("Do you want to play again(Y/N):").lower()
            if(choice != 'Y'):
                break
    else :
        print("You lose!")
        print("Computer = ",computer_guess," You = ",user_guess)
    