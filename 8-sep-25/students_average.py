'''2. Student Class with Average
 
Attributes:
 
* name → student name
* marks → list of student marks [90, 80, 85]
 
Methods:
 
* get_average() → returns average marks
* add_mark(mark) → add new score
* get_highest() → return highest mark
* get_lowest() → return lowest mark
 
Example:
 
python
s = Student("Tom", [90, 80, 85])
print(s.get_average())   # (90+80+85)/3 = 85.0
s.add_mark(95)           # marks = [90,80,85,95]
print(s.get_highest())   # 95

 
Output:
 

85.0
95'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_highest(self):
        if not self.marks:
            return None
        return max(self.marks)

    def get_lowest(self):
        if not self.marks:
            return None
        return min(self.marks)
    
s = Student("Tom", [90, 80, 85])
print(s.get_average())   
s.add_mark(95)
print(s.get_highest())   

