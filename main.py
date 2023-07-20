# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print("Welcome to te Band Name Generator.")
# city_name, pet_name = input("What's the name of the city you grew up?\n"), input("What's yours pets name?\n")
# print(f"Your band's name could be {city_name} {pet_name}")


# name_1 = input().lower().replace(" ", "")
# name_2 = input().lower().replace(" ", "")
# name_3 = name_1 + name_2
# true_count = name_3.count("t") + name_3.count("r") + name_3.count("u") + name_3.count("e")
# love_count = name_3.count("l") + name_3.count("o") + name_3.count("v") + name_3.count("e")
# total_count = int(str(true_count) + str(love_count))
#
# if total_count < 10 or total_count > 90:
#     print(f"Your score is {total_count}, you go together like coke and mentos.")
# elif 40 <= total_count <= 50:
#     print(f"Your score is {total_count}, you are alright together.")
# else:
#     print(f"Your score is {total_count}.")

name_1 = input()
name_2 = input()
name_3 = name_1.lower().replace(" ", "") + name_2.lower().replace(" ", "")
true_count = name_3.count("t") + name_3.count("r") + name_3.count("u") + name_3.count("e")
love_count = name_3.count("l") + name_3.count("o") + name_3.count("v") + name_3.count("e")
total_count = int(str(true_count) + str(love_count))

if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif 40 <= total_count <= 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
#David Beckham
#Victoria Beckham