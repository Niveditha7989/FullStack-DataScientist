'''15. Problem: Calculate electricity bill:
First 100 units → ₹5/unit
Next 100 units → ₹7/unit
Above 200 units → ₹10/unit'''


def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill
units = int(input("Enter the number of units consumed: "))
total_bill = calculate_bill(units)
print("Total electricity bill: ₹",total_bill)
