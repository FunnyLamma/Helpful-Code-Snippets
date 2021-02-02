# This is the code to make a button using the module tkinter, there are also other ways to do this, this button would close the window, tkinter is a module that opens a window on your computer, there are multiple ways to timport tkinter. #
import tkinter as tk

        self.quit = tk.Button(self, text="This is a button", fg="red",
                              command=self.master.destroy)