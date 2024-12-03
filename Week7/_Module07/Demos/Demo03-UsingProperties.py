# ------------------------------------------------- #
# Title: Demo03 - Using Properties
# Description: Demonstrates how to use class properties in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Moved the fields into the constructor
# RRoot,1.3.2030,Added properties and private attributes
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

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name  # set the attribute using the property to provide validation
        self.last_name = last_name  # set the attribute using the property to provide validation

    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()  # Optional formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # Optional validation code
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()  # Optional formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # Optional validation code
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")


# Processing --------------------------------------- #
class FileProcessor:

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            list_of_dictionary_data: list = []
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            # json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation ------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def input_data_to_table(student_data: list):
        """ This function gets data from the user and adds it to a list of dictionary rows

        :param student_data: list of dictionary rows containing our current data
        :return: list of dictionary rows filled with a new row of data
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            new_student = Student(first_name=student_first_name, last_name=student_last_name)
            student_data.append(new_student)  # This adds a student object to the list
        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)

        return student_data

    @staticmethod
    def output_student_data(student_data:list):
        for student in student_data:
            print(student.first_name, student.last_name, student)

#  End of class definitions
while True:

    # Create a list of student object rows.
    student_table = IO.input_data_to_table(student_data=student_table)

    # Display the student data in the list
    IO.output_student_data(student_data=student_table)

    if input("Add another? (y/n)".lower()) != 'y':
        break

# Save data to a file
if input("Save the data? (y/n)".lower()) == 'y':
    FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=student_table)

