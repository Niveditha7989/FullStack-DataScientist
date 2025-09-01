def reverse_string_while(s):
    reversed_s = ""
    index = len(s) - 1
    while index >= 0:
        reversed_s += s[index]
        index -= 1
    return reversed_s
str=input("Enter any string:")
reverses= reverse_string_while(str)
print(reverses)