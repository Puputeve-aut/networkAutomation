import random
# Lists are a data structure that can hold multiple values. They are ordered, mutable, and allow duplicate values. 
# Lists are defined using square brackets [] and can contain any type of data.
statesOfAmerica = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

#print(statesOfAmerica[2])
#print(statesOfAmerica[-1])  

#Using a rnadom int to choose from the list
randomStateMy = random.randint(0, len(statesOfAmerica) - 1)
print(statesOfAmerica[randomStateMy])

#Using the random.choice() method to choose from the list
randomState = random.choice(statesOfAmerica)
print(randomState) 

