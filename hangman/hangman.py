import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess your letter: ").lower()
print(chosen_word)
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        print("Right")
    else:
        print("Wrong")
