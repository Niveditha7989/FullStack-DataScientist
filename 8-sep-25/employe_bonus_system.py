'''3. Employee Bonus System
 
Attributes:
 
* name → employee name
* salary → base salary
* role → role of employee (e.g., Manager, Developer, Intern)
 
Methods:
 
* bonus() → calculates bonus depending on role:
 
  * Manager → 20% of salary
  * Developer → 10% of salary
  * Intern → 5% of salary
 
Example:
 
python
m = Manager("Alice", 50000)
print(m.bonus())

 
Output:
 

10000'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def bonus(self):
        return 0 
class Manager(Employee):
    def bonus(self):
        return self.salary * 0.20
class Developer(Employee):
    def bonus(self):
        return self.salary * 0.10
class Intern(Employee):
    def bonus(self):
        return self.salary * 0.05
m = Manager("Alice", 50000)
print(m.bonus())  
d = Developer("Bob", 60000)
i = Intern("Charlie", 20000)
print(i.bonus())  
