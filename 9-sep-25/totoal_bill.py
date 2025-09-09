'''12. Problem: Given items with prices in a dictionary, calculate total bill.'''

items={
    "maidha":50,
    "sugar":100,
    "biscuite":20

}
su=0
for i in items.values():
    su+=i
print("Total bill:",su)