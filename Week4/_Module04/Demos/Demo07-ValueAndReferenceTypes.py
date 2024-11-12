# ------------------------------------------------------------------------------------------ #
# Title: Values and Reference Types
# Desc: Shows the different behaviors of value and reference types
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
var1: None
var2: None

# -- Examples with simple data --
var1: int = 1
var2: int = var1
var1 = 3
print(var2)  # Print 1, because var1 passed the VALUE to var2!

var1: str = "Bob"
var2: str = var1
var1 = "Robert"
print(var2)  # Print "Bob", because var1 passed the VALUE to var2!

# Examples with complex collections of data
var1: list = [1, 2]  # This is a Python List collection
var2 = var1
var1[0] = 3  # The zeroth number in this collection on integers
print(var2)  # Prints [3,2], because var1 and var2 are linked by a REFERENCE!

var1 =["Bob", "Sue"]
var2 = var1
var1[0] = "Robert"  # The zeroth number in this collection of strings
print(var2)  # Prints ['Robert', Sue], because var1 and var2 are linked by a REFERENCE!

# When In Doubt, Test It Out!
var3: list = [1,2]
var4 = var3
var3 = ["A", "B"]
print(var4)  # What will this print?


var3: tuple = (1,2)
var4 = var3
var3 = ("A", "B")
print(var4)  # What will this print?











