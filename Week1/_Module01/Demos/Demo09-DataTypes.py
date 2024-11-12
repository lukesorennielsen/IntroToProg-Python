# ------------------------------------------------------------------------------------------ #
# Title: The data types
# Desc: Shows how data types work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# All variables and Constants hold one type of data at a time.
# Python automatically sets the data's type when you assign a values
data = 1  # will automatically be set as a integer data type

# The type() functions display a variables current type
print(type(data))

# Python will automatically change a variable's data type if you assign data
data = "1"  # The data is now a string data type
print(type(data))


data = 1.4  # The data is now a floating point data type
print(type(data))

data = True  # The data is now a boolean data type
print(type(data))

data = 1  # The data is now a integer data type again
print(type(data))

data = None   # The data is now empty (or null) and has a None data type
print(type(data))

# Since Python will let you change the variable's type at anytime it helps to
# indicate what type of data (datatype) it should be. In many languages this is
# do using a prefix or suffix. Here are some examples:

intData = 1  # The prefix indicates this should use integer data (Camel Casing)
BoolData = True  # The prefix indicates this should use integer data (Title Casing)
str_data = "1.4"  # The prefix indicates this should use string data (Snake Casing)
data_flt = 1.4   # The suffix indicates this should use floating point decimal data (Snake Casing)

# In later version of Python you can use Type Hints to indicate your desired datatype.
var1: str = "1.4"  # Python allows you to "suggest" a data type using a colon and the type's name
var2: float = 1.4
var3: int = 1

print(var1, var2, var3)
print(type(var1), type(var2), type(var3))

# Keep in mind that Python do no enforce you choice of data type, these are just "hints."
# Python automatically changes the variables type later if you fill it with a different type of
# data.

var1 = True  # You will NOT get an error if you do not follow the suggestion
var2 = 1
var3 = "1"

print(var1, var2, var3)
print(type(var1), type(var2), type(var3))

# Note: In this course we use type hints and snake casing for variables and constants.
# However, if your organization uses a prefix or suffix in their existing code, it is best
# practice to match that style.
