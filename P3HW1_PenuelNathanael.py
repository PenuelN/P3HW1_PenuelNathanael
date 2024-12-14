# P3HW1_PenuelNathanael.py
# This program takes grades for six modules and displays the average.

# Input: Enter grades for six modules
try:
    mod_1 = float(input('Enter grade for Module 1: '))
    mod_2 = float(input('Enter grade for Module 2: '))
    mod_3 = float(input('Enter grade for Module 3: '))
    mod_4 = float(input('Enter grade for Module 4: '))
    mod_5 = float(input('Enter grade for Module 5: '))
    mod_6 = float(input('Enter grade for Module 6: '))

    # Add the grades to a list
    grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

    # Determine the lowest, highest, sum, and average of the grades
    low = min(grades)
    high = max(grades)
    total = sum(grades)
    avg = total / len(grades)

    # Display results
    print("\n------------Results------------")
    print(f"Lowest Grade: {low:.1f}")
    print(f"Highest Grade: {high:.1f}")
    print(f"Sum of Grades: {total:.1f}")
    print(f"Average: {avg:.2f}")
    print("--------------------------------")

    # Determine and display the letter grade based on the average
    if avg >= 90:
        print("Your grade is: A")
    elif avg >= 80:
        print("Your grade is: B")
    elif avg >= 70:
        print("Your grade is: C")
    elif avg >= 60:
        print("Your grade is: D")
    else:
        print("Your grade is: F")

except ValueError:
    print("Invalid input. Please enter numeric values for grades.")



