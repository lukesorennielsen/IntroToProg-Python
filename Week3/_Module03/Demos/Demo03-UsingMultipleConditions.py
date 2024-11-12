# ------------------------------------------------------------------------------------------ #
# Title: Working with multiple conditions
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
total_grade_points : float
grade_point_average: float

# Input user data
total_grade_points = 4 + 3.6 + 3.8 + 3.2
grade_point_average = total_grade_points / 4

# Process the data
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

# You will also use Conditionals to perform different tasks based on input
strChoice = input('End the program ("y/n"): ')
if strChoice == 'y':
    quit()
else:
    input("Pausing until you use the Enter key again ...")
