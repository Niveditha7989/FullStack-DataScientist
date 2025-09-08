'''3. University System
 
Create Professor and Student classes.
 
*Professor Attributes: name, subject
 
*Professor Methods: teach(course), give_assignment(task)
 
*Student Attributes: name, courses, assignments
 
*Student Methods: enroll(course), submit_assignment(task)
 
Sample Input:
 
python
 
prof = Professor("Dr. Smith", "Computer Science")
 
stud = Student("Alice")
 
print(prof.teach("Python"))
 
print(stud.enroll("Python"))
 
print(prof.give_assignment("Project 1"))
 
print(stud.submit_assignment("Project 1"))
 

 
Sample Output:
 

 
Dr. Smith is teaching Python
 
Alice enrolled in Python
 
Dr. Smith assigned: Project 1
 
Alice submitted: Project 1
 
'''

class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def teach(self, course):
        return self.name, "is teaching", course
    def give_assignment(self, task):
        return self.name, "assigned:", task
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.assignments = []
    def enroll(self, course):
        self.courses.append(course)
        return self.name, "enrolled in", course
    def submit_assignment(self, task):
        self.assignments.append(task)
        return self.name, "submitted:", task
    
prof = Professor("Dr. Smith", "Computer Science")
stud = Student("Alice")
print(prof.teach("Python"))
print(stud.enroll("Python"))
print(prof.give_assignment("Project 1"))
print(stud.submit_assignment("Project 1"))

