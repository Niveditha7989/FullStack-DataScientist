str=input("Enter a number:")
l=len(str)
a=int(str)
b=a
sum=0
while(a>0):
    r=a%10
    sum+=r**l
    a=a//10
if(sum==b):
  print("Armstrong")
else:
  print("Not Armstrong numbre")