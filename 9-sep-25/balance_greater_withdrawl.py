'''22. Problem: If withdrawal amount is greater than balance, raise an exception.'''

def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Withdrawal amount exceeds balance!")
    else:
        balance -= amount
        return balance

balance = 1000

try:
    amount = float(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amount)
    print(f"Withdrawal successful. Remaining balance: ₹{balance}")
except Exception as e:
    print("Error:", e)
