# ------------------------------------------------------------------------------------------ #
# Title: Troubleshooting Initialization Errors
# Desc: Shows what causes initialization errors
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
message1: str = ''  # The initial value is an "empty" string
message2: str  # Not initialized

value1: int = 0  # The initial value is zero
value2: int  # Not initialized

# Process the program's data
message1 += 'More data'  # Adding data to empty string works
message2 += 'More data'  # Error: Adding data to non-initialize string

# Output the program's data
print(value1 + 5)  # Adding data to zero works!
print(value2 + 5)  # NameError: name 'value' is not defined. Did you mean: 'False'?