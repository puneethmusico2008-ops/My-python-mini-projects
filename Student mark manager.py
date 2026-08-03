
'''
   In this script we will be looking at the student work manager.
   The program allows the user to manage student work by adding, viewing, and deleting assignments.
'''
students = []
marks = []

while True:
    print("\n ====> Student Work Manager <====")
    print("1. Add student # type: ignore ")
    print("2. Display student  # type: ignore")
    print("3. Highest marks # type: ignore")
    print("4. Lowest marks # type: ignore")
    print("5. Average marks # type: ignore")
    print("6. Exit # type: ignore")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        mark = float(input("Enter student mark: "))
        students.append(name)
        marks.append(mark)
        print(f"Student {name} with mark {mark} added.")

    elif choice == '2':
        if not students:
            print("No students to display.")
        else:
            for i in range(len(students)):
                print(f"Student: {students[i]}, Mark: {marks[i]}")

    elif choice == '3':
        if not marks:
            print("No marks available.")
        else:
            highest_mark = max(marks)
            index = marks.index(highest_mark)
            print(f"Highest mark is {highest_mark} by student {students[index]}.")

    elif choice == '4':
        if not marks:
            print("No marks available.")
        else:
            lowest_mark = min(marks)
            index = marks.index(lowest_mark)
            print(f"Lowest mark is {lowest_mark} by student {students[index]}.")

    elif choice == '5':
        if not marks:
            print("No marks available.")
        else:
            average_mark = sum(marks) / len(marks)
            print(f"Average mark is {average_mark:.2f}.")

    elif choice == '6':
        print("Exiting the Student Work Manager.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

