# ------------------------------------------------------------------------------- #
# Title: Processing Classes Module
# # Description: A collection of processing classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        import json
        import sqlite3  # TODO: ADD SQLite module (Done)
except Exception as e:
    print(e.__str__())


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Converted code to use student objects instead of dictionaries
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list, student_type: object):  # TODO: Create a Student parameter (Done)
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.5.2030,Converted list of dictionaries to list of student objects

        :param file_name: string data with name of file to read from
        :param student_data: list of student rows to be filled with file data
        :param student_type: A reference to data_class.Student use to create a Student object

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(
                    file)  # the load function returns a list of dictionary rows.
                for student in list_of_dictionary_data:
                    # student_object: data.Student = data.Student(first_name=student["FirstName"],
                    #                                   last_name=student["LastName"],
                    #                                   gpa=student["GPA"])

                    student_object = student_type(first_name=student["FirstName"],
                                                  last_name=student["LastName"],
                                                  gpa=student["GPA"])

                    student_data.append(student_object)
        # TODO: Remove Dependency on presentation_classes (Done)
        except FileNotFoundError:  # as e:
            # pres.IO.output_error_messages("Text file must exist before running this script!", e)
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:  # as e:
            # pres.IO.output_error_messages("There was a non-specific error!", e)
            raise Exception("There was a non-specific error!")
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict = {"FirstName": student.first_name,
                                      "LastName": student.last_name,
                                      "GPA": student.gpa}
                list_of_dictionary_data.append(student_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)

        # TODO: Remove Dependency on presentation_classes (Done)
        except TypeError: # as e:
            # pres.IO.output_error_messages("Please check that the data is a valid JSON format", e)
            raise TypeError("Please check that the data is a valid JSON format")
        except Exception: # as e:
            # pres.IO.output_error_messages("There was a non-specific error!", e)
            raise Exception("There was a non-specific error!")


# TODO Create Database Processing Class (Done)
class DBProcessor:
    """
    A collection of processing layer functions that work with a SQLite database

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def create_connection(db_file):
        """ This function connects to a SQLite database

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param connection: string data with name of file to write to


        :return: a SQLite Connection object
        """

        try:
            con = sqlite3.connect(db_file)  # This opens OR creates the database
            print('Connected! - SQLite Version is: ', sqlite3.version)
        except Exception:
            raise ConnectionError("Please check the path and file name.")
        return con

    @staticmethod
    def select_student_data(connection: str, student_data: list, student_type: object):
        """ This function select data from the students table in a SQLite database

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param connection: string data with name of file to write to
        :param student_type: a reference to the Student class to create student objects

        :return: a list of student objects
        """
        try:
            sql: str = f"SELECT StudentID, StudentFirstName, StudentLastName, StudentGPA " \
                       f"FROM Students;"
            csr = connection.cursor()  # A cursor object allows you to submit commands
            csr.execute(sql)
            list_of_rows: list = csr.fetchall()  # fetchall puts all of the rows from the result into a list
            csr.close()  # Always close the cursor when your done

            for row_of_columns in list_of_rows:
                student = student_type()
                student.first_name = row_of_columns[1]  # Add the Id to the first name since our presentation layer do not use an ID
                student.last_name = row_of_columns[2]
                student.gpa = row_of_columns[3]
                student_data.append(student)

            return student_data
        except Exception as e:
            raise sqlite3.OperationalError("Please check arguments for extra single quotes\n", e)


    @staticmethod
    def insert_student_data(connection: str, first_name: str, last_name: str, gpa: str):
        """ This function write one row of data into the students table

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param connection: string data with name of file to write to
        :param first_name: string data with a student's first name
        :param last_name: string data with a student's last name
        :param gpa: float data with a student's grade point average

        :return: None
        """
        try:
            sql: str = f"INSERT INTO Students (StudentFirstName, StudentLastName, StudentGPA) " \
                       f"VALUES ('{first_name}', '{last_name}', {gpa});"
            csr = connection.cursor()  # A cursor object allows you to submit commands
            csr.execute(sql)  # Single quotes for strings!
            csr.execute("commit;")  # You need to add this when using PySQLite!
            csr.close()  # Always close the cursor when your done
        except Exception as e:
            raise sqlite3.OperationalError("Please check arguments for extra single quotes", e)
