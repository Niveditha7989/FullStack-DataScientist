'''21. Problem: Write a program that handles both ValueError (invalid input) and ZeroDivisionError.'''

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except ValueError:
    print("Error: Please enter valid numbers.")