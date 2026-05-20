programmingdictionary = {
    'Bug': 'An error in a program that prevents the program to running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.',
    'Loop': 'The action of doing something over and over again.'
}

#print(programmingdictionary['Bug'])

programmingdictionary['Loop'] = 'The action of doing something over and over again.'

emptyDictionary = {}

#wipe existing dictionary
#programmingdictionary = {}
#print(programmingdictionary)

programmingdictionary['Bug'] = 'A moth in your computer.'
#print(programmingdictionary['Bug'])

#Loop throught dictionary
for key in programmingdictionary:
    print(key)
    print(programmingdictionary[key])