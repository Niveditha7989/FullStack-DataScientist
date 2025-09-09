'''8. Problem: Given a dictionary of student names and attendance %, find defaulters (<75%).'''

students={
    "niveditha": 82,
    "akshaya": 67,
    "tulasi": 90
}
for name, attendance in students.items():
    if attendance < 75:
        print(name)