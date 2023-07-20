import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
string_of_letters = ""
string_of_symbols = ""
string_of_numbers = ""
total_symbols = nr_letters + nr_symbols + nr_numbers
# for letters
for rand_letter in range(0, nr_letters):
    random_letters = random.choice(letters)
    string_of_letters += random_letters

# for symbols
for rand_symbol in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    string_of_symbols += random_symbols

# for numbers
for rand_number in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    string_of_numbers += random_numbers
# print for non-random password
# print(string_of_letters, string_of_symbols, string_of_numbers, sep="")


# code for random password from non-random password
password_not_random = string_of_letters + string_of_symbols + string_of_numbers
list_pass = list(password_not_random)
final_password = ""
for final_pass in range(0, len(list_pass)):
    final_password += list_pass.pop(random.randint(0, len(list_pass) - 1))
print(final_password)
