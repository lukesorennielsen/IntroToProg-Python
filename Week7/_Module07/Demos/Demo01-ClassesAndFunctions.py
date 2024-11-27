# ------------------------------------------------- #
# Title: Demo01 - Classes and Functions
# Description: Demonstrates how to use classes and function  in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

import json

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


class Student:
    first_name: str
    last_name: str

# Processing --------------------------------------- #




# Presentation ------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """


    @staticmethod
    def input_data_to_table(student_data: list):
        """ This function gets data from the user and adds it to a list of dictionary rows

        :param student_data: list of dictionary rows containing our current data
        :return: list of student object rows filled with a new row of data
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            # Create a new student object
            new_student = Student()
            new_student.first_name = student_first_name
            new_student.last_name = student_last_name
            student_data.append(new_student)

        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)  # Prints the custom message
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)

        return student_data


#  End of class definitions
while True:
    student_table = IO.input_data_to_table(student_data=student_table)
    for student in student_table:
        print(student.first_name, student.last_name, student)
    if input("Add another? (y/n)".lower()) != 'y':
        break
