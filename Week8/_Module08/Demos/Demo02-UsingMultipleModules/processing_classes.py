# ------------------------------------------------------------------------------------- #
# Title: Application Classes Module
# # Description: A collection of processing classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# -------------------------------------------------------------------------------------- #

import json
from presentation_classes import IO

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

        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        finally:
            if file.closed == False:
                file.close()
