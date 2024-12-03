# ------------------------------------------------- #
# Title: Lab01 - Working with Properties
# # Description: Demonstrates how to use properties in a class
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Converted dictionary rows to student class objects.
# RRoot,1.3.2030,Added properties and private attributes
# <Your Name Here>,<Current Date>,Moved classes into a module
# ------------------------------------------------- #

import application_classes as ac

# TODO 1: Cut and paste the json import statement into the application_class.py code file


# TODO 2: Add an import statement to access the application_class.py code file
import application_classes as ac

# Data -------------------------------------------- #
FILE_NAME: str = '../MyLabData.json'
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:
    1. Show current student data.
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

students: list = []  # a table of student data
menu_choice = ''


# TODO 3: Cut and Paste the Person class into the application_class.py code file


# TODO 4: Cut and Paste the Student class into the application_class.py code file


# TODO 5: Cut and Paste the FileProcessor class into the application_class.py code file
# Processing --------------------------------------- #


# TODO 6: Cut and Paste the IO class into the application_class.py code file
# Presentation --------------------------------------- #


# TODO 7: Modify the main body of the script to use the application_classes module
# Beginning of the main body of this script
students = ac.FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    ac.IO.output_menu(menu=MENU)

    menu_choice = ac.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        ac.IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        students = ac.IO.input_student_data(student_data=students)
        ac.IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        ac.FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
