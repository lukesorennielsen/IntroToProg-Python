# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables,
#         operators, formatting, and files
# and calculations
# Change Log: (Who, When, What)
#   RRoot,10/21/2024,Created Script
#   Soren Nielsen,10/21/2024, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
COURSE_NAME: str = "Python 100"
COURSE_PRICE: float = 999.98
STATE_TAX: float = .09
##note that round was added to make sure we didnt display percentages of cents
TOTAL_PRICE: float = round(COURSE_PRICE + COURSE_PRICE * STATE_TAX, 2)
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str
student_last_name: str
course_name: str
csv_data: str
file_obj = none

# Get data from the user

student_first_name = input("What is your first name?")
student_last_name = input("What is your Last Name?")

# Present the data to the user
csv_data = f"{student_first_name},{student_last_name},\
{COURSE_NAME},{COURSE_PRICE},{TOTAL_PRICE}"

print(csv_data)

# Process the data to a file

file_obj = open(FILE_NAME, "w")

file_obj.write(csv_data)

#close file
file_obj.close()
print("data recorded in: " + FILE_NAME)

