# ------------------------------------------------------------------------------------------ #
# Title: Working with conditions and loops
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''


# Input the data
student_first_name = input("What is the student's first name? ")
student_last_name = input("What is the student's last name? ")
student_gpa = float(input("What is the student's GPA? "))

# Process the data to create custom messages
if student_gpa >= 4.0:
    message = "Congratulations {} {} you have earned an A with your {:.2f} GPA"
elif student_gpa >= 3.0:
    message = "Congratulations {} {} you have earned an B with your {:.2f} GPA"
elif student_gpa >= 2.0:
    message = "Congratulations {} {} you have earned an C with your {:.2f} GPA"
elif student_gpa >= 1.0:
    message = "Congratulations {} {} you have earned an D with your {:.2f} GPA"
else:
    message = "Sorry, {} {} but your {:.2f} GPA is not a passing grade"

# Output the data
print(message.format(student_first_name, student_last_name, student_gpa))

# Get input from the user before quitting the program
strChoice = input('End the program ("y/n"): ')
if strChoice == 'y':
    quit()
else:
    input("Pausing until you use the Enter key again ...")
