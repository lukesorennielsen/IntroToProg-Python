# ------------------------------------------------------------------------------------- #
# Title: Application Classes Module
# # Description: A collection of data classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# -------------------------------------------------------------------------------------- #

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
