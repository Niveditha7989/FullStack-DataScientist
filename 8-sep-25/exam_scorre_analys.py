'''2. statistics → Exam Score Analysis
 
Use statistics to calculate the mean, median, and variance of student exam scores.
 
Sample Input:
 

 
Scores = [75, 80, 90, 100, 85, 90, 95]
 

 
Sample Output:
 

 
Mean = 88.57
 
Median = 90
 
Variance = 71.43'''

import statistics

import statistics

def exam_score_analysis(scores):
    mean = round(statistics.mean(scores), 2)
    median = statistics.median(scores)
    variance = round(statistics.variance(scores), 2)
    print("Mean =", mean)
    print("Median =", median)
    print("Variance =", variance)
scores = [75, 80, 90, 100, 85, 90, 95]
exam_score_analysis(scores)

