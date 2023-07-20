def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    first_num = float(input("First number: "))
    still_counting = True
    while still_counting:
        for operation in operations:
            print(operation)
        operation_choice = input("Pick an operation: ")
        second_num = float(input("Second number: "))
        answer = operations[operation_choice](first_num, second_num)
        print(f"{first_num} + {second_num} = {answer}")
        if input("Would you like to continue? Type 'y' or 'n': ") == "y":
            first_num = answer
        else:
            still_counting = False
            calculator()


calculator()
