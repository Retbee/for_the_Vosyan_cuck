print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
first_step = input("Choose direction for the first step. You can go right, left, forward and backward: ").lower()
if first_step == "left" or first_step == "go left":
    second_step_lake = input("You turn to the left and get to the lake. You can swim it across or wait for the boat. What will you do? ").lower()
    if second_step_lake == "wait" or second_step_lake == "wait boat":
        third_step_doors = input("You have three doors before you: red, blue and yellow. Which one will you choose? ").lower()
        if third_step_doors == "red":
            print("Your ass was burnt to ashes. GG")
        if third_step_doors == "yellow":
            print("Congratulation! You've found the Treasure!")
        if third_step_doors == "blue":
            print("You've been teared apart by hungry beasts. GG")
        else:
            print("Wrong move. Death has come to you. GG")
    else:
        print("You've been eaten by giant fish right at the middle of the lake. GG")
else:
    print("You fall into a hole. GG")
