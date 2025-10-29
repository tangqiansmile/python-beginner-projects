import random

emojis = {'r':'rock','p':'paper','s':'scissors'}
game_letters = ['r','p','s']

def get_user_choice():
    while True:
        user_choice = input("enter rock or paper or scissor by 'r' or 'p' or 's'").lower()
        if user_choice in game_letters:
            return user_choice
        else:
            print(f"error, invalide choice")

def display_choices(user_choice, computer_choice):
    print(f"you chose:{emojis[user_choice]}")
    print(f"computer chose:{emojis[computer_choice]}")

def determin_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie, it is a draw!")
    elif(
        (user_choice == 'r' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'r')):
        print("computer win!")  
    else:
        print("you win!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(game_letters)

        display_choices(user_choice, computer_choice)

        determin_winner(user_choice, computer_choice)
        
        user_decision = input("do you want to continue the game? answer by y or n").lower()
        if user_decision == "n":
            print(f"let's play in next time")
            break 
        
play_game()
        

       





    
    

    
    