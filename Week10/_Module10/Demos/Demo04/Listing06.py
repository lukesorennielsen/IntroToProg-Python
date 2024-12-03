# ---------------------------------------------------------- #
# Title: Listing 06
# Description: Demonstrate using Event Handlers
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
import tkinter as tk
from tkinter import ttk

class MathProcessor(object):
    @staticmethod
    def add_w_o_params():
        print(1 + 3)

    @staticmethod
    def add_with_params(n1, n2):
        print(n1 + n2)



class MainWindow(object):

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Event Handling")
        self.window.geometry("300x110")

        # Set Event handler for custom method w/o parameters
        btn1 = ttk.Button(self.window, text="Call add_w_o_params()")
        btn1.pack(pady=5)
        btn1['command'] = MathProcessor.add_w_o_params # don't use parentheses ()

        # Set Event handler for custom method with parameters
        btn5 = ttk.Button(self.window, text="Call add_with_params")
        btn5.pack(pady=5)
        btn5['command'] = lambda: MathProcessor.add_with_params(5, 2)

        #  Set Event handler to a built-in method
        btn3 = ttk.Button(self.window, text="Quit")
        btn3.pack(pady=5)
        btn3['command'] = self.window.destroy  # don't use parentheses ()

if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()
