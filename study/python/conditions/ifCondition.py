#Write a program that welcomes people to the rollercoaster and asks for their height. 
# # If they are over 120cm, print a message that they can ride the rollercoaster, otherwise print a message that they need to grow taller before they can ride.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#If the height is 120 or more print "You can ride the rollercoaster!"
if height >= 120:
    print("You can ride the rollercoaster!")
else:    
    print("Sorry, you have to grow taller before you can ride.")