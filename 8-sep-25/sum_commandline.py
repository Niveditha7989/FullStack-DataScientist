'''5. sys → Sum from Command Line
 
Write a program using sys.argv to take three numbers from the command line and print their sum.
 
Sample Input (command line):
 

 
python add.py 5 10 15
 

 
Sample Output:
 

 
Sum = 30
 '''



import sys
if len(sys.argv) != 4:
    print("Please provide exactly three numbers.")
    sys.exit(1)
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
num3 = float(sys.argv[3])
total = num1 + num2 + num3
print("Sum =", int(total) if total.is_integer() else total)
