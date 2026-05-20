import random
# Rock Paper Scissors Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
            '''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   
          '''

# Create a list of the game images    
gameImages = [rock, paper, scissors]

# Get the user's choice
userPick = int(input("welcome to rock paper scissors! what do you choose?\nType 0 for rock, 1 for paper or 2 for scissors:  "))

# Check if the user's choice is valid
if userPick < 0 or userPick >= 3:
    print("Invalid choice! You lose.")
    exit()

# Print the user's choice
print(f"You chose: {gameImages[userPick]}")

# Randomly select the computer's choice
computerPick = random.randint(0, 2)
print(f"Computer chose: {gameImages[computerPick]}")

# Determine the winner
if userPick == computerPick:
    print("It's a tie!")
elif userPick == 0 and computerPick == 2:
    print("You win!")
elif userPick == 1 and computerPick == 0:
    print("You win!")
elif userPick == 2 and computerPick == 1:
    print("You win!")
else:
    print("You lose!")