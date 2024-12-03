# ------------------------------------------------- #
# Title: Demo01 - Using Modules
# Description: Demonstrates how to use modules in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Moved the fields into the constructor
# RRoot,1.3.2030,Added properties and private attributes
# RRoot,1.4.2030,Moved the classes into a module
# ------------------------------------------------- #

import application_classes as ac


# Data --------------------------------------------- #
FILE_NAME: str = 'MyData.json'
MENU = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current data.
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
    '''
student_table: list = []

while True:

    # Create a list of student object rows.
    student_table = ac.IO.input_data_to_table(student_data=student_table)

    # Display the student data in the list
    ac.IO.output_student_data(student_data=student_table)

    if input("Add another? (y/n)".lower()) != 'y':
        break

# Save data to a file
if input("Save the data? (y/n)".lower()) == 'y':
    ac.FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=student_table)

