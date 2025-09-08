'''5. E-commerce Order Class
 
Attributes:
 
* items → dictionary of items {name: price}
 
Methods:
 
* add(item, price) → adds an item to order
* remove(item) → removes item
* calculate_total() → returns total price of all items
* show_items() → lists all items in order
 
Example:
 
python
order = Order()
order.add("Shirt", 500)
order.add("Shoes", 1500)
print(order.calculate_total())

 
Output:
 

Total=2000
'''
class Order:
    def __init__(self):
        self.items = {}
    def add(self, item, price):
        self.items[item] = price
    def remove(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(item, "not found in order.")

    def calculate_total(self):
        total = sum(self.items.values())
        return "Total =", total

    def show_items(self):
        if not self.items:
            print("No items in order.")
        else:
            print("Items in order:")
            for item, price in self.items.items():
                print(item, ": ₹", price)
order = Order()
order.add("Shirt", 500)
order.add("Shoes", 1500)
print(order.calculate_total())

