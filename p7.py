a=int(input("Principal="))
b=int(input("Rate="))
c=int(input("Time="))
si=(a*b*c)/100
ci=a*(1+b/100)**c - a
t=input("Interest type=")
if t=="Compound":
    print("Compound Interest=",ci)
    print("Total Amount=",a+ci)
elif t=="Simple":
    print("Simple Interest=",si)
    print("Total Amount=",a+si)