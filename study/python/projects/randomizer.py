import random

randomInt = random.randint(1, 10)
#randomNumber = random.random() *10
#randomFloat = random.uniform(1, 10)

if randomInt % 2 == 0:
    print(f"Heads")
else:
    print(f"Tails")