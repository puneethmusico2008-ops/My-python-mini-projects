
'''
   This script checks if a person is eligible to vote based on their age and citizenship status.
   
   The eligibility criteria are as follows:
   1. The person must be at least 18 years old.
   2. The person must be a citizen of the country.
'''

Age = int(input("Enter your age: "))
if Age >= 18:
    Citizenship = input("Are you a citizen of the country? (yes/no): ")
    if Citizenship.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote because you are not a citizen.")
else:
    print("You are not eligible to vote because you are under 18 years old.")