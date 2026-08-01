'''
    SIMPLE GRADE CALCULATOR
    
    1.ADDITION
    2.SUBTRACTION
    3.MULTIPLICATION
    4.DIVISION
'''

A = float(input("Enter the first subject marks: "))
B = float(input("Enter the second subject marks: "))
C = float(input("Enter the third subject marks: "))
D = float(input("Enter the fourth subject marks: "))
E = float(input("Enter the fifth subject marks: "))
F = float(input("Enter the sixth subject marks: "))
total_marks = A + B + C + D + E + F
average_marks = total_marks / 6
PERCENTAGE = (total_marks / 600) * 100
print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Percentage:", PERCENTAGE, "%")

if PERCENTAGE >= 90:
    print("Grade: A+")
elif PERCENTAGE >= 80:
    print("Grade: A")   
elif PERCENTAGE >= 70:
    print("Grade: B")
elif PERCENTAGE >= 60:
    print("Grade: C")   
elif PERCENTAGE >= 50:
    print("Grade: D")   
else:
    print("Grade: F")   