import random

def get_user_choice():
         user_choice =  input("What is your choice 'r' for rock 'p' for paper or 's' for scissors\n")
         print(f'You have picked {user_choice}')
         return user_choice
         
def get_computer_choice():
        computer_choice = random.choice('r', 'p', 's') 
        return computer_choice 

def get_winner(self,computer_choice,user_choice):
        if user_choice == computer_choice:
            print("The game is a tie!")
        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                print("You have won!")
            else:
                print ('You have lost!') 
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print("You have won!")
            else:
                print("You have lost!")
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                print("You have won!")
            else:
                print("You have lost!")

def play():
    print(play)

    get_computer_choice()
    get_user_choice()
    get_winner()