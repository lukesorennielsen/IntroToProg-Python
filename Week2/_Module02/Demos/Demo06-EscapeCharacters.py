# ------------------------------------------------------------------------------------------ #
# Title: Escape Characters
# Desc: Shows how to use escape characters in a string
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
message: str

# Common escape characters include \' \" \n \t \\
print('Let\'s Test These')
print("Let's \"Test\" These")
print("Let's \\Test\\ These")
print("Let's\tTest\t\tThese")
print("Let's\nTest\nThese")

# Triple quoted string can sometimes be use instead of escape characters
message = """ | test newline
Test ' single quote 
"Test" double quote
            Test Tabs
\\ Slashes still need escaping
"""

print(message)

# Line Continuation Tests
print("test closing parentheses on new line"
      )  # Oddly, this works!

print
("test beginning parentheses on new line ")  # This does NOT work, but no error either!

print \
    ("test using the line continuation character ")  # Adding the backslash makes it work!
