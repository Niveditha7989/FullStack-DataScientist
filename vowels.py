str=input("Enter a String:")
vo=0
co=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vo+=1
    else:
        co+=1
print("vowels:",vo)
print("consonets:",co)