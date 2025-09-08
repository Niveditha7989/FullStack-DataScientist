'''1. os → Count Files by Extension
 
Write a program using os to count how many .txt and .py files are in the current directory.
 
Sample Input (files in folder):
 

 
["notes.txt", "app.py", "data.csv", "report.txt", "main.py"]
 

 
Sample Output:
 

 
Text files: 2
 
Python files: 2'''

import os

def count_files(files):
    t = 0
    p = 0
    for i in files:
        if i.endswith('.txt'):
            t += 1
        elif i.endswith('.py'):
            p += 1
    print("Text files:", t)
    print("Python files:", p)
count_files(["notes.txt", "app.py", "data.csv", "report.txt", "main.py"])
