#improve the ticket machine with age divided ticket prices.

print("Welcome to the roller coaster!")
height = int(input("How tall are you? "))
bill = 0

if height >= 120:
    print("You can ride the rollecoaster")
    age = int(input("How old are you? "))
    if age <= 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $8")
        bill = 7
    else:
        print("Adult tickets are $12")
        bill = 12
    wantsPhoto = input("Do you want to have a photo of the ride? Type y for Yes and n for No.\n")
    if wantsPhoto == "y":
        bill += 3
        print(f"your ticket is ${bill}")
        
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are not tall enough to ride")