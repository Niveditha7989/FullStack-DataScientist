str=input("Enter a string:")
w=1
c=0
v=0
for i in str:
    c+=1
    if(i==' ' or i=='\n'):
        w+=1
    elif(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v+=1
print("Total words:",w)
print("Total Characters:",c)
print("Total Vowels:",v)