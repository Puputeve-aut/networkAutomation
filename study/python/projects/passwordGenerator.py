import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
passLength = int(input("Enter the length of the password: "))
passSymbols = int(input("How many symbols would you like in your password? "))
passNumbers = int(input("How many numbers would you like in your password? "))

#easy level - order not randomised:
# password = ""
# 
# for char in range(0, passLength):
#     password += random.choice(letters)
# 
# for char in range(0, passSymbols):
#     password += random.choice(symbols)
# 
# for char in range(0, passNumbers):
#     password += random.choice(numbers)
# print("Your password is: " + password)

#hard level - order randomised:
passwordList = []

for char in range(0, passLength):
    passwordList.append(random.choice(letters))

for char in range(0, passSymbols):
    passwordList.append(random.choice(symbols))

for char in range(0, passNumbers):
    passwordList.append(random.choice(numbers))

print("\nYour password is: " + ''.join(passwordList))
random.shuffle(passwordList)
shuffledPass = ''.join(passwordList)

print(f"Your shuffled password is: {shuffledPass}")
