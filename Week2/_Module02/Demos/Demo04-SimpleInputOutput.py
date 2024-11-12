# ------------------------------------------------------------------------------------------ #
# Title: Simple data input and output
# Desc: Shows how to use the option of the print() function to display data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
first_name: str
last_name: str

# Get Data from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Displaying with print() defaults to adding an invisible space between data
print(first_name, last_name)

# You can change this by configuring the separator parameter
print(first_name, last_name, sep="-")
print("This is test message 1")  # Note the separator defaults back to space
# Also, note the second message is on a new line, due to an invisible space at the end

# You can also change the new line ending character using the end parameter
print(first_name, last_name, sep=",", end=";")
print("This is test message 2")  # Now, there is a semi-colon at the end instead
print("This is test message 3")  # Though it does change back on the next print
