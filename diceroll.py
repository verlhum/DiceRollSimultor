from random import randint as rand


def roll(rolls, sides=6):
    return [rand(1, sides) for i in range(0, rolls)]


print("Welcome to the dice rolling simluator.")

while True:
    try:
        x = input("Enter the number of dice to roll or Q to quit:")
        if x == "q":
            break
        rolls = int(x)
    except ValueError:
        print("Please enter a valid number of dice to roll.")
        continue
    check = 0
    while True:
        try:
            x = input("How many sides should each die have?:")
            sides = int(x)
            break
        except ValueError:
            print("Please enter a valid number of sides.")
    print(roll(rolls, sides))
