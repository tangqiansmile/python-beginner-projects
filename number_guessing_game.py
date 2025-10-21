import random

number_minimum = int(input("let's play a game, which number do you want to set up as minimum number?"))
number_maximum = int(input("which number do you want to set up as maximum ? "))
number_real = random.randint(number_minimum, number_maximum)

while True:
    try: 
        number_guess = int(input("which number do you want to guess"))
        if number_guess > number_real:
            print(f"too high !")
        elif number_guess < number_real:
            print(f"too low !")
        else:
            print(f"well done")
            break
    
    except ValueError:
        print(f"please enter a valid number!")