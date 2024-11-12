# ------------------------------------------------------------------------------------------ #
# Title: Variables and Constants
# Desc: Shows examples of variables and a constant
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Programs consist of data are processes
# A program holds data in memory as a variable or a constant

# Constants must contain data and that data does not change (vary)
GREETING = "Hello,"

# Variables can start as empty (without a value)
subject = None  # None indicates the variable does not have a value

# Then have a values assigned to it later
subject = "students"

# Constant and variable data can "added" together to create new data
message = GREETING + ' ' + subject  # This is called Concatenation

# You can present this data using a variable in a print function
print(message)

# Constant data stays the same, but variable data varies
subject = "teachers"
message = GREETING + ' ' + subject

# You can present this data using a variable in a print function
print(message)