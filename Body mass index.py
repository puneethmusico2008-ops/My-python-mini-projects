'''
   A ssimple program to calculate the Body Mass Index (BMI) of a person based on their weight and height.

1 Get the weight of the person in kilograms:
2 Get the height of the person in meters:
3 Calculate the BMI using the formula: BMI = weight / (height ** 2):
4 Display the calculated BMI:
'''
weight = float(input("Enter your weight in kilograms: "))   
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)    
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")   
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")     

    