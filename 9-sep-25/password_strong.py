'''2. Problem: Write a program to check if a password is strong 
(at least 8 characters, contains uppercase, lowercase, digit, 
and special char).'''
def strong_password(password):
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in special_chars for char in password)):
        return True
    else:
        return False

password = input("Enter the password: ")

if strong_password(password):
    print("Strong password")
else:
    print("Not strong")

