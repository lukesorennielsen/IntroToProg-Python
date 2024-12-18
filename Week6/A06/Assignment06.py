# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (<Soren>,<11-18-2024>,<updated to include functions and classes>)
#   RRoot,11-18-2024,Created Script
#   <Soren>,<11-18-2024>,<updated to include functions and classes>
# ------------------------------------------------------------------------------------------ #
import json

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
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.

menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

class FileProcessor:
    """
    a collection of functions that handles the reading and writing of data from files
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function handles reading data from a json file
        :param file_name: the static filename to be written to
        :param student_data: the list of data to be written
        """

        try:
            file = open(file_name, "r")

            student_data.extend(json.load(file))
            file.close()
        except FileNotFoundError as e:
            print("File was not found")
            print(e, e.__doc__, e, type(e), sep="\n")
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)
        finally:
            if  file and not file.closed:
                file.close()
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function handles writing data to the json file.
        :param file_name: The name of the file to be written to
        :param student_data: a list of data to be written to the file
        """

        try:
            file = open(file_name, "w")

            json.dump(student_data, file)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)

class IO:
    """
    A collection of functions that handles the input and output of user data
    """
    @staticmethod
    def input_menu_choice():
        """
        this function prompts the user to input a menu choice as a string input
        """
        global menu_choice
        menu_choice = input("What would you like to do: ")
    @staticmethod
    def output_menu(menu: str):
        """
        this function prints the main menu of the program for the user
        :param menu: the string that holds the printed menu
        """
        print(menu)
    @staticmethod
    def input_student_data(student_data: list):
        """
        This function manages the input of student data
        :param student_data: the list of data to be updated
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            students_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(students_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        this function handles printing error messages
        :param message: the custom error message to be printed to the console
        :param error: the error data
        """
        print(message)
        print("-- Technical Error Message -- ")
        print(error)
        print(type(error))
        print(error.__doc__)
        print(error.__str__())
    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays student data to the user.
        :param student_data: the list of student data to be printed.
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)



FileProcessor.read_data_from_file(FILE_NAME, students)
# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(MENU)
    IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
