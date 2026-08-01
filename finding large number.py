'''
   FINDING THE LARGEST NUMBER AMONG THREE NUMBERS
   This program takes three numbers as input from the user and determines which one is the largest.
'''

A= int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))

if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C

print("The largest number is:", largest)    