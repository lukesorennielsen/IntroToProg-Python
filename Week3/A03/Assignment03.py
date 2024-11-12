# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Soren, 10/28/2024, Initial)
#   RRoot,10/28/2024,Created Script
#   Soren,10/28/2024, Created
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = \
    "---- Course Registration Program ----\n\
  Select from the following  menu:\n\
    1. Register a Student for a Course\n\
    2. Show current data\n\
    3. Save data to a file\n\
    4. Exit the program\n\
-----------------------------------------"

FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj = None
menu_choice: str = "0"

# Present and Process the data

print(MENU)

# Present the menu of choices

menu_choice = input("What would you like to do?: ")

while menu_choice != 4:

    # Input user data

    if menu_choice == "1":
        student_first_name = input("Student's First Name: ")
        student_last_name = input("Student's Last Name: ")
        course_name = input("What is the course name?: ")
        print(f"{student_first_name} {student_last_name} has been added to {course_name}")
        csv_data += f"{student_first_name},{student_last_name},{course_name}\n"

    # Present the current data

    elif menu_choice == "2":
        print(f"the current data is:\n" + csv_data)

    # Save the data to a file

    elif menu_choice == "3":
        file_obj = open(FILE_NAME, "w")
        file_obj.write(csv_data)
        print(f"{csv_data} written to {FILE_NAME}")
        file_obj.close()

    # Stop the loop

    elif menu_choice == "4":
        print("Program Ended")
        exit()

    print(MENU)
    menu_choice = input("What would you like to do?: ")










