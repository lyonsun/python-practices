import math
import random


def getNumberInput(prompt, min=0):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input <= min:
                print(f"Please enter a number greater than {min}!")
            else:
                break
        except ValueError:
            print("Please enter a number!")
    return user_input


def guess():
    print("\n\tWelcome to the maddy number guess game!\n")

    lower = getNumberInput("Enter lower bound: ")
    upper = getNumberInput("Enter upper bound: ", lower)
    answer = random.randint(lower, upper)
    max_count = round(math.log(upper - lower + 1, 2))
    count = 0

    print(f"\n\tYou have only {max_count} chances to win the game.\n")

    for _ in range(0, max_count):
        guess = getNumberInput("What is your guess: ")

        if guess < answer:
            print("Your guess is too small, try again.")
        elif guess > answer:
            print("Your guess is too large, try again.")
        else:
            print(f"Congratulations! You made it in {count+1} try!")
            break

        count += 1

    if count >= max_count:
        print(
            f"\n\tYou are running out of {max_count} avaiable chances. The answer is {answer}, better luck next time!\n"
        )


if __name__ == "__main__":
    guess()
