#Pizza proce calculator for study nesting and chaining if statements
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do ypu want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extraCheese = input("Do you want extra cheese on your pizza? Y or N: ")
price = 0


if size == "S":
    price = 15

elif size == "M":
    price = 20 

elif size == "L":
    price = 25

else:
    print("You typed the wrong inputs")
    
    
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extraCheese == "Y":
    price += 1
    
print(f"Your pizza is ${price}")



