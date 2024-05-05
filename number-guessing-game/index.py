import math
import random


while True:
    try:
        lower = int(input("Enter lower bound: "))
        if lower <= 0:
            print("Please enter a positive number!")
        else:
            break
    except ValueError:
        print("Please enter a number!")

while True:
    try:
        upper = int(input("Enter upper bound: "))
        if upper <= lower:
            print(f"Please enter a number bigger than the lower bound {lower}!")
        else:
            break
    except ValueError:
        print("Please enter a number!")

answer = random.randint(lower, upper)
max_count = round(math.log(upper - lower + 1, 2))
count = 0

print(f"\n\tYou have only {max_count} chances to win the game.\n")

for _ in range(0, max_count):
    count += 1

    while True:
        try:
            guess = int(input("What is your guess: "))
            break
        except ValueError:
            print("Please enter a number!")

    if guess < answer:
        print("Your guess is too small, try again.")
    elif guess > answer:
        print("Your guess is too large, try again.")
    else:
        print(f"Congratulations you made it in {count} try!")
        break


if count >= max_count:
    print(
        f"\n\tYou are running out of {max_count} avaiable chances. The answer is {answer}, better luck next time!\n"
    )
