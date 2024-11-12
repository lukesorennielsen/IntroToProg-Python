# ------------------------------------------------------------------------------------------ #
# Title: Assignment01
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Soren 10/14/2024)
#   RRoot,10/14/2024,Created Script
#   Soren Nielsen,10/14/2024, Created Script
# ------------------------------------------------------------------------------------------ #

#establish course name

COURSE_NAME = "Python 100"

#prompt student for name input

student_first_name = input("What is your first name? ")
student_last_name = input("What is your last name? ")

#linebreak for visual clarity
print()

#prints the students name and their course

print("your name is: " +  student_first_name + " "
      + student_last_name + ". You are registered for: " + COURSE_NAME)

#linebreak for visual clarity
print()

#print a second time with \n line breaks

print("your name is:\n " +  student_first_name + " "
      + student_last_name +  " \nYou are registered for:\n " + COURSE_NAME)
