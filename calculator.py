'''
    SIMPLE CALCULATOR IN PYTHON
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
'''
print("select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == '1':
    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))
    result = int(num1) + int(num2)
    print("The result is: "+ str(result))
elif operation == '2':
    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))
    result = int(num1) - int(num2)
    print("The result is: "+ str(result))
elif operation == '3':
    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))
    result = int(num1) * int(num2)
    print("The result is: "+ str(result))
elif operation == '4':
    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))
    if int(num2) != 0:
        result = int(num1) / int(num2)
        print("The result is: "+ str(result))
    else:
        print("Error: Division by zero is not allowed.")  