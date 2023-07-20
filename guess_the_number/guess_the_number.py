import random


def choose_difficulty():
    while True:
        choice = input("Welcome to the 'Guess number' game! Type 'easy' to choose easy mode or 'hard' to choose "
                       "hard mode: ").lower()
        if choice == "easy":
            return 10
        elif choice == "hard":
            return 6
        else:
            print("Invalid output! Please type 'easy' or 'hard'!")


def try_to_guess(lives, guessed_num):
    list_of_guesses = []
    while lives > 0:
        try:
            guess_attempt = int(input("Type your guess: "))
            list_of_guesses.append(guess_attempt)
        except ValueError:
            print("Please type only integer numbers!!!")
            continue
        if guess_attempt < guessed_num:
            print(f"Too low. Your live score is: {lives - 1}")
            lives -= 1
        elif guess_attempt > guessed_num:
            print(f"Too high. Your live score is: {lives - 1}")
            lives -= 1
        else:
            print(f"Congratulations! Guessed number was {guessed_num}. Your live score is: {lives}. Your attempts were: {list_of_guesses}")

    else:
        print(f"You lost. Guessed number was: {guessed_num}. Your live score is: {lives}. Your attempts were: {list_of_guesses}")
        return


def main():
    lives = choose_difficulty()
    guessed_num = random.randint(0, 100)
    try_to_guess(lives=lives, guessed_num=guessed_num)


if __name__ == "__main__":
    main()
