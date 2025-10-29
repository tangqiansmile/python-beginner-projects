import random

emojis = {'r':'rock','p':'paper','s':'scissors'}
game_letters = ['r','p','s']

while True:
    user_choice = input("enter rock or paper or scissor by 'r' or 'p' or 's'").lower()
    if user_choice not in game_letters:
        print(f"error, invalide choice")
        continue #jump back to while loop

    computer_choice = random.choice(game_letters)

    print(f"you chose:{emojis[user_choice]}, computer chose:{emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie, it is a draw!")
    elif(
        (user_choice == 'r' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'r')):
        print("computer win!")  
    else:
        print("you win!")
       
    user_decision = input("do you want to continue the game? answer by y or n").lower()
    if user_decision == "n":
        print(f"let's play in next time")
        break
    
