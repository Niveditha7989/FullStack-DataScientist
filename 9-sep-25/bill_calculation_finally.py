'''23. Problem: Calculate total price, handle invalid input, and always show "Bill processing finished".
• First 100 units → ₹5/unit
• Next 100 units → ₹7/unit
• Above 200 units → ₹10/uni'''


def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

try:
    units = int(input("Enter the number of units consumed: "))
    if units < 0:
        raise ValueError("Units cannot be negative.")
    
    total = calculate_bill(units)
    print(f"Total bill amount: ₹{total}")
    
except ValueError as ve:
    print("Invalid input:", ve)

finally:
    print("Bill processing finished.")
