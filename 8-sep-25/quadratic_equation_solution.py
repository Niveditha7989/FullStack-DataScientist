'''3. math → Quadratic Equation Solver
 
Use the math module to solve quadratic equations of the form ax² + bx + c = 0.
 
Sample Input:
 

 
a = 1, b = -3, c = 2
 

 
Sample Output:
 

 
Roots are: 1.0 and 2.0
 
'''

import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("Roots are:", root1, "and", root2)
    elif d == 0:
        root = -b / (2 * a)
        print("Roots are:", root, "and", root)
    else:
        print("No real roots")
solve_quadratic(1, -3, 2)
