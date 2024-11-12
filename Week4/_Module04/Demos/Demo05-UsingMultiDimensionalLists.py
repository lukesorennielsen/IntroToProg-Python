# ------------------------------------------------- #
# Title: Demo04 - Using Tuples and Lists
# Description:  This script demonstrates using multi-dimensional lists to hold data
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# Two one-dimensional lists (like a row of data)
student01: list = ["Vic", "Vu"]
student02: list = ["Sue", "Jones"]

# Display the default representation of a list
print("\nDefault list representation:", student01)

# Accessing elements using indexing
print("First element of the list:", student01[0])  # First column in the table

# A two-dimensional list (like a table of data)
students = [["Vic", "Vu"], ["Sue", "Jones"]]

# Display the default representation of a list
print("\nDefault list representation:", students)

# Displaying the variable's type and memory address
print("List type:", type(students))

# Accessing elements using indexing
print("First element of the list:", students[0])  # First row of the table

# Default presentation of a two-dimensional list
print("Custom list presentation:", students)

# Custom presentation of a list
custom_presentation = f"{students[0][0]} {students[0][1]}, {students[1][0]} {students[1][1]}"
print("Custom list presentation:", custom_presentation)

# Displaying the variable's type and memory address
print("List type:", type(students))
print("List memory address:", id(students))

# Adding an element to a list
students.append(["Tim", "Thomas"])

# Displaying the updated list
print("List after adding an element:", students)




