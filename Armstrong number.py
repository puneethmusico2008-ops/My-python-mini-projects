
'''
This scripts checks whether a given number is an Armstrong number or not.
An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
The program prompts the user to enter a number and then checks if it is an Armstrong number.
'''

num = int(input("Enter a number to check if it is an Armstrong number: "))
# Convert the number to a string to easily iterate over its digits  
num_str = str(num)

for digit in num_str:
    # Calculate the number of digits in the number
    num_digits = len(num_str)
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    for i in range(len(num_str)):
        digit = int(num_str[i])
        armstrong_sum += digit ** num_digits

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")