#Password Generator Project - Study Test
import random

# Declaring the global variables:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = []
password_numbers = []
password_symbols = []

randomised_password = ""

# Add the quantity of letters, numbers or symbols to each correspondent variable as asked by the user.
for letter in range(0, nr_letters):
  password_letters.append(random.choice(letters))
for number in range(0, nr_numbers):
  password_numbers.append(random.choice(numbers))
for symbol in range(0, nr_symbols):
  password_symbols.append(random.choice(symbols))

# Concatenate the list variables for letters, numbers and symbols
concatenated_password = password_letters + password_numbers + password_symbols

# Randomize the list generated with the variable concatenated_password above
random.shuffle(concatenated_password)

# Turn the List concatenated_password into a String, inside the randomised_password variable
for char in concatenated_password:
  randomised_password += char

print(f"Your generated password is: {randomised_password}")
