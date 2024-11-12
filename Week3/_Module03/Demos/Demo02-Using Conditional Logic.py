# ------------------------------------------------------------------------------------------ #
# Title: Conditional Logic Statements
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
message: str
student_first_name: str
student_last_name: str
student_gpa: float


# Output the data
student_first_name = input("What is the student's first name? ")
student_last_name = input("What is the student's last name? ")
student_gpa = float(input("What is the student's GPA? "))

# You will often use conditional logic to display different output
if student_gpa >= 4.0:
    message = "Congratulations {} {} you have earned an A of with your {:.2f} GPA"
else:
    message = "Congratulations {} {} on your {:.2f} GPA"

print(message.format(student_first_name, student_last_name, student_gpa))

# You will also use Conditionals to perform different tasks based on input
strChoice = input('End the program ("y/n"): ')
if strChoice == 'y':
    quit()
else:
    input("Pausing until you use the Enter key again ...")
