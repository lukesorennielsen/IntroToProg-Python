# ------------------------------------------------------------------------------------- #
# Title: Application Classes Module
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# -------------------------------------------------------------------------------------- #
import json  # This will only import if the exception is not thrown.

# Data  --------------------------------------- #
class Person:

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Student(Person):

    def __init__(self, first_name: str = "", last_name: str = "", gpa: float = 0.0):
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name=first_name,last_name=last_name)
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float):
        try:
            self.__gpa = float(value)
        except ValueError:
            raise ValueError("GPA must be a numeric value.")

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.gpa}"


# Processing --------------------------------------- #
class FileProcessor:

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "GPA": student.gpa}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
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

            student_gpa = float(input("Enter the student's gpa: "))
            new_student = Student(first_name=student_first_name, last_name=student_last_name, gpa=student_gpa)

            student_data.append(new_student)
        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)

        return student_data

    @staticmethod
    def output_student_data(student_data:list):
        for student in student_data:
            print(student.first_name, student.last_name, student.gpa)