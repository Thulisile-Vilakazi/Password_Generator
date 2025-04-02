import random
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 
    '{', '|', '}', '~'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = []

print("Let's generate a random password for you")
num_letters = input("How many letters should the password have? ")
num_symbols = input("How many symbols should the password have? ")
num_nums = input("How many numbers should the password have? ")

for char in range(1, int(num_letters)):
    password.append(random.choice(letters))

for char in range(1, int(num_symbols)):
    password.append(random.choice(symbols))

for char in range(1, int(num_nums)):
    password.append(random.choice(numbers))

password = random.shuffle(password)

print(f" Your password is {password}")
