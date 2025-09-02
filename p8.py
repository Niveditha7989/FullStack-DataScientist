a=input("Message=")
b=int(input("Shift="))
c=""
for i  in a:
    c+=chr(ord(i)+b)
print("Encrypted Message= ",c)