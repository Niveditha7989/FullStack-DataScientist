'''4. Problem: Given a list of student names, find duplicates.'''

students = ['akshaya', 'nivedditha', 'tulasi', 'akshaya', 'akshaya', 'divya']

duplicates = []

for name in students:
    if students.count(name) > 1 and name not in duplicates:
        duplicates.append(name)

print("Duplicate names are:", duplicates)
