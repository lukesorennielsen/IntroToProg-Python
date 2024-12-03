# ------------------------------------------------- #
# Title: Lab01 - Working with Properties
# # Description: Demonstrates how to use properties in a class
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Converted dictionary rows to student class objects.
# RRoot,1.3.2030,Added properties and private attributes
# RRoot,1.4.2030,Moved classes into a modules
# RRoot,1.5.2030,Moved classes into separate modules
# ------------------------------------------------- #

# ---------------------------------------------------
# NOTE: This is the Answer to Mod08-Lab-03
# ---------------------------------------------------

import processing_classes as proc
import presentation_classes as pres


# Data -------------------------------------------- #
FILE_NAME: str = 'MyData.json'
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


# Beginning of the main body of this script
students = proc.FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        pres.IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        students = pres.IO.input_student_data(student_data=students)
        pres.IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        proc.FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
