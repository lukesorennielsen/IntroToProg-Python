# ------------------------------------------------------------------------------------------ #
# Title: CSV Files
# Desc: Shows how format data in a file using comma separators
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
current_directory: str
file_reference: object
first_name: str
last_name: str
email: str

# This code will show you the current working directory. This is helpful for troubleshooting and
# can be removed or commented out later.
import os
current_directory = os.getcwd()
print("Current working directory:", current_directory)


# open a connection to a file (and make a new one if it does not exist)
file_reference  = open("_Data.csv", "w")


# Get user input
first_name = "Bob"
last_name = "Smith"
email = "BSmith@Gomail.com"

# Save the input data to the file
file_reference.write(f"{first_name},{last_name},{email}\n")

# Get more user input
first_name = "Tim"
last_name = "Tsu"
email = "TTsu@Gomail.com"

# Save the input data to the file
file_reference.write(f"{first_name},{last_name},{email}\n")

# Close the connection and finish saving the data in the file
file_reference.close()















