import random
from wordList import wordList
from hangmanArt import hangman, logo


chosenWorld = random.choice(wordList)
print(logo)
lives = 6

placeholder = ''
wordLenght = len(chosenWorld)

for position in range(wordLenght):
    placeholder += "_"
print('Word to guess: ' + placeholder)

gameOver = False
correctLetters = []
wrongLetters = []
s = ","

while not gameOver:
    print(f'\n******************You have {lives} remaining******************\n')
    guess = input('Guess a letter: ').lower()
    
    if guess in correctLetters:
        print(f'You already guessed  {guess}')
    
    display = ''

    for char in chosenWorld:
        if char == guess:
            display += char
            correctLetters.append(guess)
        elif char in correctLetters:
            display += char
        else:
            display += "_"
                
    if guess not in chosenWorld:    
        print(f'"{guess}" is not in the word')
        if guess not in wrongLetters:
            lives -= 1
            wrongLetters.append(guess)
        elif guess in wrongLetters:
            print(f'You already guessed {guess}')
    
    if lives == 0:
        gameOver = True
        print(f"******************It was {chosenWorld}! You Lose!******************")
            

    if "_" not in display:
        gameOver = True
        print("******************You win!******************")
    
    
    badLetters = s.join(wrongLetters)
    print(hangman[lives])         
    print(f'letters not in word: {badLetters}')
    print(f'\nWord to guess: {display}')
    
    