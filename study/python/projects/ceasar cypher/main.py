from icon import logo
from cipher import ceasar

shouldContinue = True

while shouldContinue:
    print(logo)
    direction = input('type "encrypt" to encrypt, type "decode" to decrypt: \n')
    text = input('Type your messeage: ').lower()
    shift = int(input('Type ths shift number: '))
    
    ceasar(originalText=text, shiftAmount=shift,encodeOrDecode=direction)
    
    restart =input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        shouldContinue = False
        print("Goodbye")