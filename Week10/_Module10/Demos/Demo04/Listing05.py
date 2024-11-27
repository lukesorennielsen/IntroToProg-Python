# ---------------------------------------------------------- #
# Title: Listing 05
# Description: Creates a Windowed UI
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
import tkinter as tk
from tkinter import ttk   # Updated look and feel

class MainWindow(object):
    """  Description: Creates the following UI objects:

    window_root (tk.TK):
        lbl_math_info (ttk.label):
        btn_add (ttk.button):
        btn_subtract (ttk.button):
    """
    @staticmethod
    def create_main_window():
        application_window = tk.Tk()
        application_window.geometry("400x100")
        application_window.title("Simple Math")

        lbl_math_results = ttk.Label(application_window, text="Math Results")
        lbl_math_results.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

        btn_add = ttk.Button(application_window, text="Add", width=10)
        btn_add.grid(row=2, column=1, sticky=tk.NW, padx=10, pady=5)

        btn_subtract = ttk.Button(application_window, text="Subtract", width=10)
        btn_subtract.grid(row=2, column=2, sticky=tk.NW, padx=5, pady=5)

        return application_window
# End class

if __name__ == '__main__':
    mw = MainWindow.create_main_window()
    mw.mainloop()
