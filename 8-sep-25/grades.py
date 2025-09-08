'''4. Grade Calculator
 
* Function takes marks and returns grade.
 
* Input: [85, 90, 78]
 
* Output: "Grade: A"'''
def grades(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return "Grade: A+"
    elif avg >= 80:
        return "Grade: A"
    elif avg >= 70:
        return "Grade: B"
    elif avg >= 60:
        return "Grade: C"
    elif avg >= 50:
        return "Grade: D"
    else:
        return "Grade: F"
print(grades([85, 90, 78]))
