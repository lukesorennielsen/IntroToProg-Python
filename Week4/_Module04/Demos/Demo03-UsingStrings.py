# ------------------------------------------------- #
# Title: Demo03 - Using strings
# Description:  This script demonstrates using indexes and functions on strings
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# Data --------------------------------------------- #
student1: str = "Bob,Baker"

# Processing --------------------------------------- #
# Using len() to count the characters in the string
string_length = len(student1)
print(f"The length of the string is {string_length} characters.")

# Accessing the first character (character 'B') using an index
first_character = student1[0]
print(f"The first character is: {first_character}")

# Using a slice to extract the first three characters
first_three_characters = student1[0:3]
first_three_characters = student1[:3]
print(f"The first three characters are: {first_three_characters}")

# Using a slice to extract the first name
first_name = student1[:student1.index(',')]
print(f"The first name is: {first_name}")

# Using a slice to extract the last nam
comma_index = student1.index(',')
last_name = student1[comma_index + 1:]
print(f"The last name is: {last_name}")

# Using split() to separate the string into parts using a comma as the delimiter
student_data = student1.split(',')
print("Student Data:")
print(f"First Name: {student_data[0]}")
print(f"Last Name: {student_data[1]}")


