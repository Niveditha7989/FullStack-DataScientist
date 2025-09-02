a=(input("PIN="))
b=int(input("Balance="))
c=int(input("Withdraw="))
if a=="1234":
    if c<=b:
        print("PIN Verified")
        print("Withdraw Successful.Remaining Balance=",b-c)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")