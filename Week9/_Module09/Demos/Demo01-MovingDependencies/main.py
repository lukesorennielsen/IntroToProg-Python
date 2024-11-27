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
# TODO: Add as Reference Argument to Student (Done)
try:
    students = proc.FileProcessor.read_data_from_file(file_name=data.FILE_NAME,
                                                      student_data=data.students,
                                                      student_type=data.Student)
except FileNotFoundError as e:
    pres.IO.output_error_messages(e)
except Exception as e:
    pres.IO.output_error_messages(e)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        pres.IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
                                           # TODO: Add as Reference Argument to Student (Done)
        students = pres.IO.input_student_data(student_data=students, student_type=data.Student)
        pres.IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        proc.FileProcessor.write_data_to_file(file_name=data.FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
