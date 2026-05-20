alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(originalText, shiftAmount, encodeOrDecode):
    outputText = ''
    
    if encodeOrDecode == "decode":
        shiftAmount *= -1

    for letter in originalText:
        if letter not in alphabet:
            outputText += letter
        else:
            shiftedPosition = alphabet.index(letter) + shiftAmount
            shiftedPosition %= len(alphabet)
            outputText += alphabet[shiftedPosition]
        
    print(f'Here is the {encodeOrDecode}d result: {outputText}')