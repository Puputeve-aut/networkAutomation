import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():
    isRunning = True
    print(logo.logo)
    num1 = float(input("Give me the first number: "))

    while isRunning:
        for symbol in operations:
            print(symbol)     
            
        operationSymbol = input("Pick an operation: ")
        num2 = float(input("Give me the next number: "))
        answare = operations[operationSymbol](num1,num2)
        print(f"{num1} {operationSymbol} {num2} = {answare}")
        
        choice = input(f"Type 'y' to continue calculationg with {answare}, or type 'n' to start new calculation, for exit type 'q': ").lower()
        
        if choice == "y":
            num1 = answare
        elif choice == "n":
            isRunning = False
            print("\n" * 50)
            calculator()
        else:
            return



calculator()