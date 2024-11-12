# ------------------------------------------------------------------------------------------ #
# Title: Mod02-Lab01-Concatenation with multiple types
# Desc: This lab demonstrates concatenation
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define the program's data
student_first_name: str = "Vic"
student_last_name: str = "Vu"
student_gpa: float = 3.9

# Output the data
message_str = "Student " + student_first_name + " " + student_last_name
message_str += " has a " + str(student_gpa) + " grade point average (GPA)"

print(message_str)
