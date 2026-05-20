#Write a program that calculates the tip for a restaurant bill. 
# The program should ask for the total bill, the percentage tip the user would like to give, and the number of people to split the bill between. The program should then calculate the total amount each person should pay and print it out.
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

#Calculate the tip amount and the total amount per person
tip_amount = total_bill * tip_percentage / 100
total_amount = total_bill + tip_amount
amount_per_person = total_amount / number_of_people

#Print the amount each person should pay, rounded to 2 decimal places
print(f"Each person should pay: ${amount_per_person:.2f}")