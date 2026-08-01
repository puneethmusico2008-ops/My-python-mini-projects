'''
   Sum of first N natural numbers
   This program calculates the sum of the first N natural numbers using a loop.
'''

num = int(input("Enter a positive integer N to calculate the sum of first N natural numbers: "))
if num < 1:
    print("Please enter a positive integer greater than 0.")
else:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print("The sum of the first", num, "natural numbers is", sum)
    