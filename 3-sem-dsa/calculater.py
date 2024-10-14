class Calculator:
    
    def __init__(self):
        pass
    
    # Method for addition
    def add(self, a, b):
        return a + b
    
    # Method for subtraction
    def sub(self, a, b):
        return a - b
    
    # Method for multiplication
    def multiply(self, a, b):
        return a * b
    
    # Method for division
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            return a / b

def calculator_program():
    calc = Calculator()  
    while True:
        operation = input("Enter operation (add, sub, multiply, divide) or 'quit' to exit: ").lower()
        
        if operation == 'quit':
            print("Exiting the calculator.")
            break
        
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        
        if operation == 'add':
            print("Result:", calc.add(a, b))
        elif operation == 'subtract':
            print("Result:", calc.subtract(a, b))
        elif operation == 'multiply':
            print("Result:", calc.multiply(a, b))
        elif operation == 'divide':
            print("Result:", calc.divide(a, b))
        else:
            print("Invalid operation. Please try again.")
        
        print()  

calculator_program()
