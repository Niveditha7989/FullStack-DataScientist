'''1. Bank Account Class
 
Attributes:
 
* `balance` → stores the current money in the account
* `owner` (optional) → name of account holder
 
Methods:
 
* `deposit(amount)` → adds money to balance
* `withdraw(amount)` → subtracts money if enough funds
* `get_balance()` → returns balance
 
Example:
 
```python
acc = BankAccount(100)   # initial balance = 100
acc.deposit(50)          # balance = 150
acc.withdraw(30)         # balance = 120
print(acc.get_balance())
```
 
Output:
 
```
Balance: 120
```
 '''

class BankAccount:
    def __init__(self, balance, owner="Unknown"):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:",amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return "Balance: ",self.balance
    
acc = BankAccount(100)   
acc.deposit(50)          
acc.withdraw(30)        
print(acc.get_balance()) 
