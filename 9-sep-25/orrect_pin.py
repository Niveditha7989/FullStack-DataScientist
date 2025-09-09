'''19. Problem: User has 3 attempts to enter correct PIN.'''

correct_pin="1234"
attempts=3
while attempts!=0:
    pin=input("Enter the pin:")
    if(pin==correct_pin):
        print("correct pin")
        break
    else:
        attempts-=1
if attempts==0:
    print("try again")