# ------------------------------------------------- #
# Title: Example Main Module
# Description: Demonstrates how to import classes and functions from a module
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
import example_module as em  # Note we are using a alias

# Calling a standalone function
em.standalone_function()

# Creating an object from a class
objMD = em.MyData()

# Calling static methods in two classes
em.FileProcessor.process_data()
em.IO.print_data()
