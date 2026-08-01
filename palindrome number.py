
'''
this script depicts the process of checking if a number is a palindrome.
 A palindrome is a number that reads the same backward as forward.
'''

number = int(input("Enter a number to check if it is a palindrome: "))
original_number = number

for i in range(1):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10

    if original_number == reversed_number:
        print(original_number, "is a palindrome.")
    else:
        print( "is not a palindrome.") 