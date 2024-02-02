import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")#Title of the gui window
        #Create select source button
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positon entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #creates button to select the destination of files
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #grid the postion for the button to be under select source
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Postitons entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))
        #button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #postition of the transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0, 15))
        #exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
    #Function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0,END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
    #Function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the entry widget
        #allows the path to be inserted into the Entry widtet properly
        self.destination_dir.delete(0,END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)
    
    #function to transfer files from one directory
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #gets destination directory
        destination = self.destination_dir.get()
        #goes through each file in folder checking if has been modifed in the last 24 hours
        for i in source_files:
            dir_source = os.path.join(source, i)
            dir_destination = os.path.join(destination, i)
            current_time = datetime.now()
            lmtime = datetime.fromtimestamp(os.path.getmtime(dir_source))
            time_difference = current_time - lmtime
            #if the file has been modified in the last 24 hours transfer it
            if time_difference < timedelta(hours=24):
                shutil.move(dir_source, dir_destination)
                print(i + 'was successfully transferred.')
             
    #function to exit program
    def exit_program(self):
        #root is the main GUI window
        #destroy tells python to terminate root and all the widgets inside
        root.destroy()
        












if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
