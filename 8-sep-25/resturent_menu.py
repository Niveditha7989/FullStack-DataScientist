'''5. Restaurant Menu
 
Create a Menu class with:
 
*Attributes: items (dict → item: price)
 
*Methods:
 
* add_item(name, price)
 
* remove_item(name)
 
* update_price(name, new_price)
 
* show_menu()
 
Sample Input:
 
python
 
menu = Menu()
 
print(menu.add_item("Burger", 100))
 
print(menu.add_item("Pizza", 200))
 
print(menu.update_price("Pizza", 250))
 
print(menu.remove_item("Burger"))
 
menu.show_menu()
 

 
Sample Output:
 

 
Burger added
 
Pizza added
 
Pizza price updated to 250
 
Burger removed
 
Menu: {'Pizza': 250}
 
'''



class Menu:
    def __init__(self):
        self.items = {}
    def add_item(self, name, price):
        self.items[name] = price
        return name, "added"
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return name, "removed"
        else:
            return name, "not found"
    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            return name, "price updated to", new_price
        else:
            return name, "not found"
    def show_menu(self):
        print("Menu:", self.items)
menu = Menu()
print(menu.add_item("Burger", 100))
print(menu.add_item("Pizza", 200))
print(menu.update_price("Pizza", 250))
print(menu.remove_item("Burger"))
menu.show_menu()
