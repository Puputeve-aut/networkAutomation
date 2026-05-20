height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(round(bmi, 2))

# This was not part of the project but I wanted to add it in to make it more useful. 
# It gives you a little bit of information about your bmi and tells you if you are underweight, normal weight, overweight or obese.

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
elif bmi < 40:
    print("You are severely obese.")
else:    print("You are morbidly obese.")