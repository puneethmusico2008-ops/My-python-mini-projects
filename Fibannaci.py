'''
   counting fibonacci numbers using recursion and iteration.
   This program calculates the Fibonacci numbers up to a certain limit using both recursion and iteration.
'''
terms = int(input("Enter the number of terms for Fibonacci sequence: "))

first = 0
second = 1

print("first", first)
print("second", second)

for i in range(2, terms):
    next = first + second
    print("next", next)
    first = second
    second = next
    
