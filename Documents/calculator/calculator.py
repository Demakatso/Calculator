import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def modulo(a, b):
    return a % b

def calculator():
    print("Welcome to the Python Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square root")
        print("7. Modulo")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ")
        
        if choice == '8':
            print("Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4', '5', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {modulo(num1, num2)}")
        
        elif choice == '6':
            try:
                num1 = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            print(f"√{num1} = {sqrt(num1)}")
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    calculator()