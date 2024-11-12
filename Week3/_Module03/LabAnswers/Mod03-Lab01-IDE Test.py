# ------------------------------------------------------------------------------------------ #
# Title: Mod03-Lab01-Testing the IDE
# Desc: This lab demonstrates that the IDE is installed and working
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define and initialize the program's data
student_first_name: str
student_last_name: str
student_gpa: float
message: str

# Input the data
student_first_name = input("What is the student's first name? ")
student_last_name = input("What is the student's last name? ")
student_gpa = float(input("What is the student's GPA? "))

# Output the data
message = f"Student {student_first_name } {student_last_name}"
message += f" has a {student_gpa:.2f} grade point average (GPA)"
print(message)

