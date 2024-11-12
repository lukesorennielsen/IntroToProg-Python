# ------------------------------------------------------------------------------------------ #
# Title: Mod02-Lab03-SavingDataToCSVFiles
# Desc: This lab demonstrates using input and output to a file
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
"""
Lab Notes:
* Use the f-string to format the data
* Enter the following data: Vic Vu, 3.9 GPA and Sue Jones, 4.0
"""

# Define the program's data
message: str
file_reference: object
student_first_name: str
student_last_name: str
student_gpa: float

# Define the starting data
# TODO: ADD CODE HERE
message = "Student {}{}"
message += " has a {:.2f} grade point average (GPA)"

# Open a file for data processing
# TODO: ADD CODE HERE
file_reference = open("_LabData.csv", "w")

# Capture data input for the first student
# TODO: ADD CODE HERE
student_first_name = input("What is the student's first name? ")
student_last_name = input("What is the student's last name? ")
student_gpa = input("What is the student's GPA? ")

# Format the captured data
# TODO: ADD CODE HERE
message = f"{student_first_name},{student_last_name},{student_gpa}\n"

# Write the new data string to the CSV file
# TODO: ADD CODE HERE
file_reference.write(message)
print("Data Recorded!\n")

# Capture data input for the second student
# TODO: ADD CODE HERE
student_first_name = input("What is the student's first name? ")
student_last_name = input("What is the student's last name? ")
student_gpa = input("What is the student's GPA? ")

# Format the captured data
# TODO: ADD CODE HERE
message = f"{student_first_name},{student_last_name},{student_gpa}\n"

# Write the new data string to the CSV file
# TODO: ADD CODE HERE
file_reference.write(message)
print("Data Recorded!\n")

# Close the file to save the data
# TODO: ADD CODE HERE
file_reference.close()

# Now, look at the file to see if it worked
