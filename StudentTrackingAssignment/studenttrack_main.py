#Python Ver: 3.11.5
#
#Author: Garrett Hiles
#
#Purpose: Student tracking demo. Using OOP, tkinter UI, tkinker with parent and
#child relationships
#
#Tested on Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox


#import other files connected
import studenttrack_gui
import studenttrack_func

#Frame is the Tkinter frame class that our own class will inherit form
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define the master frame configuration
        self.master = master
        self.master.minsize(500,300) #height, width
        #CenterWindow method will center the app on the users screen
        
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        #this protocal method is built in tkinkter method that catches if the user
        #clicks the X in the upper corner
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttrack_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module
        #keeping code comparmentalized and clutter free
        studenttrack_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
