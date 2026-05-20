def greet():
    print("Welcome, Traveler")
    print("This is a function")
    print("Have a nive day!")

#Function that alloves for input

def greetWithName(name):
    print(f"Welcome, {name}")
    print("This is a function")
    print(f"Have a nive day {name}!")
    
#Function with more than 1 input

def greetWith(name, location):
    print(f"Welcome, {name}")
    print(f"How is the weather in {location}")
    print(f"Have a nive day {name} from {location}!")
     
greetWith(location='Hollywood', name= 'George')
