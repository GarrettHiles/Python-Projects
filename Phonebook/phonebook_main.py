#Python Ver: 3.11.5
#
#Author: Garrett Hiles
#
#Purpose: Phonebook demo. Using OOP, tkinter UI, tkinker with parent and
#child relationships
#
#Tested on Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox


#import other files connected
import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit form
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define the master frame configuration
        self.master = master
        self.master.minsize(500,300) #height, width
        self.master.maxsize(500,300)
        #CenterWindow method will center the app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("the Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #this protocal method is built in tkinkter method that catches if the user
        #clicks the X in the upper corner
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module
        #keeping code comparmentalized and clutter free
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
