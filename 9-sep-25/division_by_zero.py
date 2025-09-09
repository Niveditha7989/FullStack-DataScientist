'''20. Problem: Write a program that asks for two numbers and divides them. Handle division by zero.'''


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except:
    print("Error: Division by zero is not allowed.")

