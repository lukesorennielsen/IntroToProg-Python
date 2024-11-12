# ------------------------------------------------------------------------------------------ #
# Title: Mod02-Lab02-Formatting
# Desc: This lab demonstrates using the format() function
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
"""
Lab Notes:
* Use the format() function or f-string instead of concatenation
* Use the following data: Vic Vu, 3.9 GPA and Sue Jones, 4.0 GPA
"""

# Define the program's data
student_first_name: str = "Vic"
student_last_name: str = "Vu"
student_gpa: float = 3.9
message: str


# Output program data
message = "Student {} {} has a {:.2f} grade point average (GPA)"
print(message.format(student_first_name, student_last_name, student_gpa))

# OR
message = "Student {} {} has a {:.2f} grade point average (GPA)"
print(message.format(student_first_name, student_last_name, student_gpa))

# OR

print(f"Student {student_first_name } {student_last_name} has a {student_gpa:.2f} grade point average (GPA)")

