# ------------------------------------------------- #
# Title: Demo02 - Working with json files
# Description: Write and Reading file data using json
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
import json
from io import TextIOWrapper

# Data --------------------------------------------- #
student_row1: dict[str, str] = {
    "FirstName": "Vic",
    "LastName": "Vu",
    "IsRegistered": True,
    "GPA": 3.7,
}
student_row2: dict[str, str] = {
    "FirstName": "Sue",
    "LastName": "Salias",
    "IsRegistered": False,
    "GPA": 3.2,
}
student_table: list[dict[str, str]] = [student_row1, student_row2]
file: TextIOWrapper = None
file_data: str = ""

# Processing --------------------------------------- #
# Write to the  file

# CSV
file = open("MyData.csv", "w")
for each in student_table:
    string_row = (
        f'{each["FirstName"]},{each["LastName"]},{each["IsRegistered"]},{each["GPA"]}\n'
    )
    file.write(string_row)
file.close()


# JSON automatically with json module
file = open("MyData.json", "w")
json.dump(student_table, file)
file.close()


# Note the function dump[s] convert the list of dictionary rows into a string.
json_data = json.dumps(student_table)
print(json_data, type(json_data))
print(student_table, type(student_table))


# Read from the CSV file
file = open("MyData.csv", "r")
for each_row in file.readlines():
    student_data = each_row.strip().split(",")
    student_data = {
        "FirstName": student_data[0],
        "LastName": student_data[1],
        "IsRegistered": student_data[2],
        "GPA": student_data[3],
    }
    # Load it into our collection (list of lists)
    student_table.append(student_data)
file.close()


# Read from the JSON file
file = open("MyData.json", "r")
student_table = json.load(file)
for item in student_table:
    print(
        f'{item["FirstName"]} {item["LastName"]} has a gpa of {item["GPA"]} '
        f'and has a registration status of {item["IsRegistered"]}'
    )
file.close()
