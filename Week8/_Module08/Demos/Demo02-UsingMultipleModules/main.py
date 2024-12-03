# ------------------------------------------------- #
# Title: Demo01 - Using Modules
# Description: Demonstrates how to use modules in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Moved the fields into the constructor
# RRoot,1.3.2030,Added properties and private attributes
# RRoot,1.4.2030,Moved the classes into a module
# RRoot,1.5.2030,Moved the module into a package
# ------------------------------------------------- #

import processing_classes as proc
import presentation_classes as pres

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
    student_table = pres.IO.input_data_to_table(student_data=student_table)

    # Display the student data in the list
    pres.IO.output_student_data(student_data=student_table)

    if input("Add another? (y/n)".lower()) != 'y':
        break

# Save data to a file
if input("Save the data? (y/n)".lower()) == 'y':
    proc.FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=student_table)
