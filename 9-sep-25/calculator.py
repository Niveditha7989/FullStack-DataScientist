'''3. Problem: Implement a calculator with +, -, *, / operations.'''
op1=float(input("Enter the operand1:"))
op2=float(input("Enter the operand2:"))
operator=input("Enter the operator +,-,*,/,%:\n")
if operator=='+':
    print(op1+op2)
elif operator=='-':
    print(op1-op2)
elif operator=='*':
    print(op1*op2)
elif operator=='/':
    print(op1/op2)
elif operator=='%':
    print(op1%op2)