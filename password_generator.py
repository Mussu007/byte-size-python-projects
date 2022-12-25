import random

print("Welcome to the PyPassword Generator!")

user_input_lenght = int(input("How long would you like in your password?: "))
user_input_uppercase_letters = int(input("How many uppercase letters would you like in your password?: "))
user_input_lowercase_letters = int(input("How many lowercase letters would you like in your password?: "))
user_input_numbers = int(input("How many numbers would you like in your password?: "))
user_input_symbols = int(input("How many symbols would you like in your password?: "))

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

password = ""
for characters in range(1, user_input_lenght+1):
    for upper in range(1, user_input_uppercase_letters+1):
        random_upper = random.choice(UPPERCASE_CHARACTERS)
        password += random_upper
    for lower in range(1, user_input_lowercase_letters+1):
        random_lower = random.choice(LOWERCASE_CHARACTERS)
        password += random_lower
    for symbol in range(1, user_input_symbols+1):
        random_symbol = random.choice(SYMBOLS)
        password += random_symbol
    for digit in range(1, user_input_numbers+1):
        random_digit = random.choice(DIGITS)
        password += random_digit

print(f"Here is your password!: {password}")