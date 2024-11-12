# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And JSON Files
# Desc: Shows how work with dictionaries and json files when using a table of data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
FILE_NAME: str = 'MyLabData.json'

# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''
FILE_NAME = "MyLabData.json"
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ''  # Holds a custom message string
menu_choice: str = ''   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Not using type hint helps PyCharm, so we won't use it going forward

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# file = open(FILE_NAME, "r")
# for row in file.readlines():
#     # Transform the data from the file
#     student_data = row.split(',')
#     student_data = {"FirstName": student_data[0],
#                     "LastName": student_data[1],
#                     "GPA": float(student_data[2].strip())}
#     # Load it into our collection (list of lists)
#     students.append(student_data)
# file.close()

file = open(FILE_NAME, "r")
students = json.load(file)
file.close()

# Repeat the follow tasks
while True:

    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

    if menu_choice == "1":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
        continue

    elif menu_choice == "2":
        # Input the data
        student_first_name = input("What is the student's first name? ")
        student_last_name = input("What is the student's last name? ")
        student_gpa = float(input("What is the student's GPA? "))
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": student_gpa}
        students.append(student_data)
        continue

    elif menu_choice == "3":
        #  Save the data to the file
        # file = open(FILE_NAME, "w")
        # for student in students:
        #     file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
        # file.close()
        # print("Data Saved!")

        #  Save the data to the file
        file = open(FILE_NAME, "w")
        json.dumps(students, file)
        file.close()
        continue

    elif menu_choice == "4":
        break  # out of the while loop

