# ------------------------------------------------------------------------------------- #
# Title: Application Classes Module
# # Description: A collection of presentation classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# -------------------------------------------------------------------------------------- #

from data_classes import Student

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
            student_gpa = float(input("Enter the student's gpa: "))
            new_student = Student(first_name=student_first_name, last_name=student_last_name, gpa=student_gpa)

            student_data.append(new_student)
        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)

        return student_data

    @staticmethod
    def output_student_data(student_data: list):

        for student in student_data:
            print(student.first_name, student.last_name, student.gpa)
