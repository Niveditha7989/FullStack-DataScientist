'''10. Problem: Write a function to check if a number is prime.'''

n=int(input("Enter number:"))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if c==2:
    print("Given number",n," is prime")
else:
    print("Not a prime number")