'''
  Factorial of a number
  This program calculates the factorial of a given number using recursion.
'''

num = int(input("Enter a number to calculate its factorial: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("The factorial of", num, "is", factorial)

