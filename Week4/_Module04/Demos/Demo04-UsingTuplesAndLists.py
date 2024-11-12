# ------------------------------------------------- #
# Title: Demo04 - Using Tuples and Lists
# Description:  This script demonstrates using tuples and lists to hold data
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# Demonstrating tuples
student01: tuple = ("Vic", "Vu")

# Display the default representation of a tuple
print("Default tuple representation:", student01)

# Accessing elements using indexing
print("First element of the tuple:", student01[0])

# Custom presentation of a tuple
custom_presentation = f"{student01[0]}, {student01[1]}"
print("Custom tuple presentation:", custom_presentation)

# Displaying the variable's type and memory address
print("Tuple type:", type(student01))
print("Tuple memory address:", id(student01))

# Adding an element to a tuple
student01 += (4.0,)

# Displaying the updated tuple
print("Tuple after adding an element:", student01)

# Displaying the variable's type and new memory address
print("Updated tuple type:", type(student01))
print("Updated tuple memory address:", id(student01))
# Note this is a different object with a new memory address since tuples are immutable!


# Demonstrating lists
student_list = ["Sue", "Jones"]

# Display the default representation of a list
print("\nDefault list representation:", student_list)

# Accessing elements using indexing
print("First element of the list:", student_list[0])

# Custom presentation of a list
custom_presentation = f"{student_list[0]}, {student_list[1]}"
print("Custom list presentation:", custom_presentation)

# Displaying the variable's type and memory address
print("List type:", type(student_list))
print("List memory address:", id(student_list))

# Adding an element to a list
student_list += [4.0]

# Displaying the updated list
print("List after adding an element:", student_list)

# Displaying the variable's type and memory address (same object same memory address)
print("Updated list type:", type(student_list))
print("Updated list memory address:", id(student_list))

# Adding an element to a list with the append() function (only works with lists)
student_list.append("A")
# Displaying the updated list
print("List after adding an element:", student_list)