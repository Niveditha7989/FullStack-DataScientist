''' 2. ATM Machine with PIN
 
Create an ATM class with:
 
*Attributes: balance, pin, is_authenticated
 
*Methods:
 
* login(pin) → checks PIN
 
* check_balance()
 
* deposit(amount)
 
* withdraw(amount)
 
Sample Input:
 
python
 
atm = ATM(1234, 500)
 
print(atm.login(1234))
 
print(atm.deposit(200))
 
print(atm.withdraw(100))
 
print(atm.check_balance())
 

 
Sample Output:
 

 
Access Granted
 
Deposited 200
 
Withdrew 100
 
Balance: 600
 '''



class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.is_authenticated = False

    def login(self, pin):
        if pin == self.pin:
            self.is_authenticated = True
            return "Access Granted"
        else:
            return "Invalid PIN"

    def check_balance(self):
        if self.is_authenticated:
            return "Balance:", self.balance
        else:
            return "Please login first"

    def deposit(self, amount):
        if self.is_authenticated:
            self.balance += amount
            return "Deposited", amount
        else:
            return "Please login first"

    def withdraw(self, amount):
        if self.is_authenticated:
            if amount <= self.balance:
                self.balance -= amount
                return "Withdrew", amount
            else:
                return "Insufficient balance"
        else:
            return "Please login first"
atm = ATM(1234, 500)
print(atm.login(1234))
print(atm.deposit(200))
print(atm.withdraw(100))
print(atm.check_balance())
