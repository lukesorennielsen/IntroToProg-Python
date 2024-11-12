# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
csv_data: str = ""  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
csv_table_data: list[str] = [""]

isfirstrun = True
file_obj = open(FILE_NAME, "r")
for row in file_obj.readlines():
    student_data = row.split(",")
    student_data = [student_data[0],student_data[1],student_data[2].strip()]

    if isfirstrun:
        csv_table_data = [student_data]
        isfirstrun = False
    else:
        csv_table_data.append(student_data)

## confirma and feedback data import
print ("inherited data from .csv is:")
index = 0
for each in csv_table_data:
    print(f"Index {index} is: {csv_table_data[index]}")
    index +=1


# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        csv_data = [student_first_name,student_last_name,course_name]
        csv_table_data.append(csv_data)
        print (f"Added Student: {csv_data}")
        continue

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        index = 0
        for each in csv_table_data:
            print(csv_table_data[index])
            index += 1
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file_obj = open(FILE_NAME, "w")

        index = 0
        for each in csv_table_data:
            string_data = (f"{csv_table_data[index][0]},{csv_table_data[index][1]},{csv_table_data[index][2]}")
            file_obj.write(string_data)
            file_obj.write("\n")
            index += 1



        file_obj.close()
        print("data updated")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
