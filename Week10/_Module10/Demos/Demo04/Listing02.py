# ---------------------------------------------------------- #
# Title: Listing02
# Description: Creates the following UI objects
#  -- window_root tk.TK
#   -- lbl_math_info (tk.label)
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
import tkinter as tk

# Create a root node Window object
application_window = tk.Tk()
application_window.geometry("400x100")  # Define the size of the window

# Create a label object in the Window and get a reference
lbl_math_results = tk.Label(application_window, text="Math Results")

# add to the root container using the pack "layout Manager" method
lbl_math_results.pack()

# Display the window
application_window.mainloop()
