# ---------------------------------------------------------- #
# Title: Listing 07
# Description: Demonstrate getting data from Entry textboxes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
import tkinter as tk
from tkinter import ttk

class MathProcessor(object):
    @staticmethod
    def add(n1, n2): print(n1 + n2)

    @staticmethod
    def subtract(n1, n2): print(n1 - n2)

    @staticmethod
    def multiply(n1, n2): print(n1 * n2)

    @staticmethod
    def divide(n1, n2): print(n1 / n2)

class MainWindow(object):
    """  Description: Creates the following UI objects:
    window_root (tk.TK)
        lbl_math_info (ttk.label)
        txt_first_number (ttk.entry)
        txt_second_number (ttk.entry)
        btn_add (ttk.button)
        btn_subtract (ttk.button)
        btn_multiply (ttk.button)
        btn_divide (ttk.button)
    """

    @staticmethod
    def create_main_window():
        """ Create  and configure a root node Window object"""
        application_window = tk.Tk()
        application_window.geometry("450x120")
        application_window.title("Simple Math")

        lbl_math_results = ttk.Label(application_window, text="Math Results")
        lbl_math_results.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

        lbl_first_number = ttk.Label(
            application_window,
            text="First Number ",
            width=20,
            anchor=tk.E
        )
        lbl_first_number.grid(row=2, column=1, sticky=tk.E)
        txt_first_number = ttk.Entry(application_window, width=40)
        txt_first_number.grid(row=2, column=2, columnspan=3)
        txt_first_number.insert(0, "0.00")

        lbl_second_number = ttk.Label(
            application_window,
            text="Second Number ",
            width=20,
            anchor=tk.E
        )
        lbl_second_number.grid(row=3, column=1, sticky=tk.E)
        txt_second_number = ttk.Entry(application_window, width=40)
        txt_second_number.grid(row=3, column=2, columnspan=3)
        txt_second_number.insert(0, "0.00")

        btn_add = ttk.Button(application_window, text="Add", width=10)
        btn_add.grid(row=4, column=1, sticky=tk.NE, padx=5, pady=5)
        btn_add['command'] = lambda: MathProcessor.add(
            float(txt_first_number.get()), float(txt_second_number.get())
        )

        btn_subtract = ttk.Button(application_window, text="Subtract", width=10)
        btn_subtract.grid(row=4, column=2, sticky=tk.NW, padx=5, pady=5)
        btn_subtract['command'] = lambda: MathProcessor.subtract(
            float(txt_first_number.get()), float(txt_second_number.get())
        )

        btn_multiply = ttk.Button(application_window, text="Multiply", width=10)
        btn_multiply.grid(row=4, column=3, sticky=tk.NW, padx=0, pady=5)
        btn_multiply['command'] = lambda: MathProcessor.multiply(
            float(txt_first_number.get()), float(txt_second_number.get())
        )

        btn_divide = ttk.Button(application_window, text="Divide", width=10)
        btn_divide.grid(row=4, column=4, sticky=tk.NW, padx=5, pady=5)
        btn_divide['command'] = lambda: MathProcessor.divide(
            float(txt_first_number.get()), float(txt_second_number.get())
        )

        return application_window
# End class

if __name__ == '__main__':
    mw = MainWindow.create_main_window()
    mw.mainloop()
