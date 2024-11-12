# ------------------------------------------------------------------------------------------ #
# Title: Creating Strings of Characters
# Desc: Shows how data types work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the program's data
string_of_data: str

# Work with the data
# A String is a collection of individual characters (They are just called strings).
string_of_data = "a string of data"

# When you add new data to a variable it deletes the old and creates a new
string_of_data = "a new string of data"

# You can print a single character by indicating its number in the sequence
print(string_of_data[2])  # Prints out a since the numbers start at zero

# You can see each the character using something called a for loop
for each_character in string_of_data:
    print(each_character, sep=" ", end="|")

# We will learn more about how the for loop works later!
