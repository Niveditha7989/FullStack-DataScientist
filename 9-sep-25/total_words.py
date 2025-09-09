'''1. Problem: Given a text file, count the total number of words.'''

a=open("file1.txt","r")
re=a.read()
words=re.split(' ')
print("No of words are:",len(words))


