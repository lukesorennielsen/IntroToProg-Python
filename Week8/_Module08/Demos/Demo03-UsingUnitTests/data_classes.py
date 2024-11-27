# ------------------------------------------------------------------------------- #
# Title: Data Classes Module
# # Description: A collection of data classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #

class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.

    ChangeLog:
        - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
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
            raise ValueError("The last name should not contain numbers.")


    @property
    def last_name(self):
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")


    def __str__(self):
        return f'{self.first_name},{self.last_name}'


# TODO 2: Cut and Paste the Student class into the data_classes.py code file
class Student(Person):
    """
    A class representing student data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        gpa (float): The gpa of the student.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.3.2030,Added properties and private attributes
    RRoot,1.3.2030,Moved first_name and last_name into a parent class
    """

    def __init__(self, first_name: str = '', last_name: str = '', gpa: float = 0.00):
        super().__init__(first_name=first_name, last_name=last_name)
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float):
        try:  # using a try block to capture when an input cannot be changed to a float
            # self.__gpa = float(value)
            self.__gpa = value

        except ValueError:
            raise ValueError("GPA must be a numeric value.")

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.gpa}'
