import cv2 
import time
from keras.models import load_model
import numpy as np
import random 
model = load_model('keras_model.h5', compile = False)


class RPS:
    def __init__(self):
        self.user_choice = ""
        self.computer_choice = ""
        self.comp_wins = 0
        self.user_wins = 0
        self.max_score = 3
        self.all_options = {0:"Rock",1:"Paper",2:"Scissors",3:"Nothing"}




    def get_prediction(self):
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            all_options = {0:"nothing",1:"paper",2:"scissors",3:"rock"}
            start = time.time()
            maxtime = 5 
            while time.time() < start + maxtime:
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                cv2.imshow('frame', frame)
# Press q to close the window
                max_value_index = np.argmax(prediction[0],axis=0)
                user_choice = all_options[max_value_index] 
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                elif time.time() == maxtime:
                    return user_choice
            
# After the loop release the cap object
            cap.release()
# Destroy all the windows
            cv2.destroyAllWindows()
            return str(user_choice) 


    def get_computer_choice(self):
        choice = ['rock','paper','scissors']
        computer_choice = random.choice(choice)
        return computer_choice 

    def get_winner(self,user_choice,computer_choice):
        print(f"The computer has chosen {computer_choice} and you have chosen {user_choice}")
        if user_choice == computer_choice:
            result = ("The game is a tie!")
            print(result)
        elif user_choice == 'rock':
            if computer_choice == 'scissors': 
                result = ("You have won!")
                print(result)
            else:
                result = ('You have lost!') 
                print(result)
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                result = ("You have won!")
                print(result)
            else:
                result = ("You have lost!")
                print(result)
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                result = ("You have won!")
                print(result)
            else:
                result = ("You have lost!")
                print(result) 
    
    def three_rounds(self,outcome): 
        self.comp_wins = 0
        self.user_wins = 0
        self.max_score = 3
        while not (self.comp_wins == 3 or self.user_wins == 3):
            computer_choice = RPS.get_computer_choice(self)
            user_choice = RPS.get_prediction(self)
            outcome = RPS.get_winner(self,user_choice,computer_choice)
            if outcome == "You have won!":
                self.user_wins += 1
            elif outcome == "You have lost!":
                self.comp_wins += 1
            else:
                pass
        if self.comp_wins == self.max_score and self.comp_wins > self.user_wins:
            print("Computer wins the game")
        elif self.user_wins == self.max_score and self.user_wins > self.comp_wins:
            print("You have won the game")
        else:
            pass
        print(f"The final scores are {self.comp_wins} and {self.user_wins}") 
        cv2.destroyAllWindows()

    def play(self):
        computer_choice = RPS.get_computer_choice
        user_choice = RPS.get_prediction
        RPS.get_winner(self,user_choice,computer_choice)
        RPS.three_rounds(self,outcome=any)  
        

game = RPS()
game.play()