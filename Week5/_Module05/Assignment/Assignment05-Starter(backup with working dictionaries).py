# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Soren, 11/11/2024, updated to use exception handling and dictionaries)
#   RRoot,1/1/2030,Created Script
#   <Soren Nielsen>,<11/11/2024>, <updated to use exception handling and dictionaries>
# ------------------------------------------------------------------------------------------ #
from fileinput import close

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"


# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str, str, str] = {"first_name": "", "last_name": "", "course_name": ""}
students: list[dict[str, str, str]] = []
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
file_obj = open(FILE_NAME, "r")
for row in file_obj.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = {"first_name": student_data[0], "last_name": student_data[1], "course_name": student_data[2].strip()}
    # Load it into our collection (list of lists)
    students.append(student_data)
file_obj.close()
print(type(students))
print(type(student_data))
print(students)
# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_data = {"first_name": student_first_name, "last_name": student_last_name, "course_name": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        print(students)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        for student in students:
            csv_data = f"{student["first_name"]},{student["last_name"]},{student["course_name"]}\n"
            file.write(csv_data)
        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student["first_name"]} {student["last_name"]} is enrolled in {student["course_name"]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
quit()
