# ------------------------------------------------------------------------------------------ #
# Title: Working with multiple conditions
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
grade: float = 0
total_grade_points : float = 0
grade_point_average: float = 0
counter: int = 0
choice: str = ''

# Input user data using is the assignment operator
while True:
    grade = float(input("Enter a grade: "))
    total_grade_points += grade
    counter += 1

    choice = input("Add another? ('y/n'): ")
    if choice.lower() == 'y':
        continue
    else:
        break

# Process the data
grade_point_average = total_grade_points / counter

if grade_point_average >= 4.0:
    message = " A GPA of {:.2f} equals an A"
elif grade_point_average >= 3.0:
    message = "A GPA of {:.2f} equals a B"
elif grade_point_average >= 2.0:
    message =  "A GPA of {:.2f} equals a C"
elif grade_point_average >= 1.0:
    message =  "A GPA of {:.2f} equals a D"
else:
    message = "A GPA of {:.2f} is not a passing grade"

# Present the results
print(message.format(grade_point_average))
