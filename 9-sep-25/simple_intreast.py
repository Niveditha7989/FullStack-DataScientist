'''7. Problem: Calculate Simple Interest.'''

def simple_interest(p, r, t):
    interest = (p * r * t) / 100
    return interest
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))
SI = simple_interest(P, R, T)
print("Simple Interest =", SI)

