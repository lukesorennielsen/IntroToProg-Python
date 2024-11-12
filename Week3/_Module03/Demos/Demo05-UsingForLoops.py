# ------------------------------------------------------------------------------------------ #
# Title: Working with multiple conditions
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
grade: float = 0
list_of_grade_points: str
total_grade_points : float = 0
grade_point_average: float = 0
counter: int = 0

# Input user data using is the assignment operator
list_of_grade_points = input("Enter grades separate by a comma (ex. 4.0,3.5, 3.6) :")
print("You Entered:", list_of_grade_points)

for grade in list_of_grade_points.split(','):  # Using split to separate the values
    total_grade_points += float(grade)
    counter += 1

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
