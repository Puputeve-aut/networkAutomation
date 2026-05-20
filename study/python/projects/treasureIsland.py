#Its a "fun" trasure island game with basic if statements and path selection.
print("Welcome to the treasure island!\nYour mission is to fint the treasure.")
crossroad =input("You're at a cross road. where do you want to go?\n        Type 'left' or 'right'\n")


if crossroad == "left":
    wait = input("\nYou arrive at the beach, do you want to wait for a boat or swim?\n       Type 'swim' or 'wait'\n")
    if wait == "wait":
        door = input("\nThe boat has taken you to the island succesfully.\nYou face three doors on the island, red, yellow, blue.\nChoose a door: ")
        if door == "yellow":
            print("\nYou find the treasure!")
        
        elif door == "red" or door == "blue":
            print("\nNothing behind this door, you lost.\n")
        
        else:
            print("\nThere is no door like that.\n")
        
    elif wait == "swim":
        print("\nYou try to swim but the sharks catch you. You lost.\n")
        
    else:
        print("\nThere is no such option.\n")    
        
elif crossroad == 'right':
    print("\nSorry wrong direction, you lose\n")
    
else:
    print("\nThere is no such direction.\n")