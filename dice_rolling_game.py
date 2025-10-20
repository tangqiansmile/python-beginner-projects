#loop
  # ask: roll the dice?
  # if enter yes
       # generate two random numbers
  # if enter no
       # thanks your message
       # terminate the game 
  #  if enter other else
 # print invalid choice
import random

while True:
    choice = input("roll the dice ? (answer by y(yes) or n(no))").lower()
    if choice == "y":
        dice_times = int(input("how many dices do you want to roll? answer from 1 to 10"))
        roll_times = 0
        for i in range(1,dice_times + 1):
            dice = random.randint(1,6)
            roll_times = roll_times + 1
            print(f"dice{roll_times},{dice},")
    elif choice == "n":
        print(f"thanks for your message")
        break
    else:
        print(f"invalid choice")
