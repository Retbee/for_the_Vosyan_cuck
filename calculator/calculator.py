result = [0]


def operators():
    operators_string = "+\n-\n*\n/\n"
    return operators_string


operators_output = operators()
start_counting = False
still_counting = False


def start_count(first_number, second_number, operation):
    if operation == "+":
        total = first_number + second_number
        print(f"{first_number} + {second_number} = {total}")
    elif operation == "-":
        total = first_number - second_number
        print(f"{first_number} - {second_number} = {total}")
    elif operation == "*":
        total = first_number * second_number
        print(f"{first_number} * {second_number} = {total}")
    else:
        total = first_number / second_number
        print(f"{first_number} / {second_number} = {total}")
    result.append(total)


while not start_counting:
    first_number = float(input("What's the first number: "))
    print(operators_output)
    operation = input("Pick an operation: ")
    second_number = float(input("What's the second number: "))
    start_count(first_number=first_number, second_number=second_number, operation=operation)
    do_not_stop_counting = input("Would like to continue counting with the result? Type 'yes' or 'no': ")

    if do_not_stop_counting == "yes":
        start_counting = True

while not still_counting:
    previous_result = result[-1]
    print(operators_output)
    operation = input("Pick an operation: ")
    second_number = float(input("What's the second number: "))
    start_count(first_number=previous_result, second_number=second_number, operation=operation)
    do_not_stop_counting = input("Would like to continue counting with the result? Type 'yes' or 'no': ")

    if do_not_stop_counting == "no":
        still_counting = True
