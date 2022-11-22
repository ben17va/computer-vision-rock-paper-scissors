import random

def get_user_choice():
    while True:
        choice = ['r','p','s']
        user_choice =  input("What is your choice 'r' for rock 'p' for paper or 's' for scissors\n")
        print(f'You have picked {user_choice}')
        if user_choice in choice:
            return user_choice

def get_computer_choice():
    choice = ['r','p','s']
    computer_choice = random.choice(choice).lower
    return computer_choice 

def get_winner(computer_choice,user_choice):
        if user_choice == computer_choice:
            print("The game is a tie!")
        elif user_choice == 'r':
            if computer_choice == 's':
                print("You have won!")
            else:
                print ('You have lost!') 
        elif user_choice == 'p':
            if computer_choice == 'r':
                print("You have won!")
            else:
                print("You have lost!")
        elif user_choice == 's':
            if computer_choice == 'p':
                print("You have won!")
            else:
                print("You have lost!")

def play():

    computer_choice = get_computer_choice
    user_choice = get_user_choice
    get_winner(computer_choice,user_choice)

play()

