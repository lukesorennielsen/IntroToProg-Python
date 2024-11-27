# ------------------------------------------------- #
# Title: Lab01 - Working with Properties
# # Description: Demonstrates how to use properties in a class
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

try:
    if __name__ == "__main__":
        import processing_classes as proc
        import presentation_classes as pres
        import data_classes as data
    else:
        raise Exception("This file starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())


# Beginning of the main body of this script
try:
    # students = proc.FileProcessor.read_data_from_file(file_name=data.FILE_NAME,
    #                                                   student_data=data.students,
    #                                                   student_type=data.Student)

    # TODO: Create an open connection to the database (Done)
    db_con = proc.DBProcessor.create_connection(db_file=data.DB_FILE_PATH)
    # TODO: Get a list of student objects from the database (Done)
    data.students = proc.DBProcessor.select_student_data(connection=db_con
                                                         , student_data=data.students
                                                         , student_type=data.Student)

except ConnectionError as e:  # TODO: ADD DB Error Handling (Done)
    pres.IO.output_error_messages(e)
except FileNotFoundError as e:
    pres.IO.output_error_messages(e)
except Exception as e:
    pres.IO.output_error_messages(e)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.DB_MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        pres.IO.output_letter_by_gpa(student_data=data.students)
        continue

    elif menu_choice == "2":  # Enter new data (and display the change)
                                           # TODO: Add as Reference Argument to Student (Done)
        data.students = pres.IO.input_student_data(student_data=data.students, student_type=data.Student)

        # TODO: Add code to save data the database (Done)
        # Get the newly entered row
        last_row = data.students[len(data.students) - 1]
        # Save data in a Database
        proc.DBProcessor.insert_student_data(connection=db_con
                                            ,first_name=last_row.first_name
                                            ,last_name=last_row.last_name
                                            ,gpa=last_row.gpa
                                            )

        # Now Display the data
        pres.IO.output_letter_by_gpa(student_data=data.students)

        continue

    # elif menu_choice == "3":
    #     # Save data in a file
    #     proc.FileProcessor.write_data_to_file(file_name=data.FILE_NAME, student_data=data.students)
    #     continue

    # TODO: Change to option 3 (Done)
    elif menu_choice == "3":  # End the program
        break  # out of the while loop
