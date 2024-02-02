import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=1, padx=(10,10), pady=(10,10))
        #Button to submit the custom text
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.SubmitCustom)
        self.btn.grid(row=3, column=2, padx=(10,10), pady=(10,10))
        #Creates string variable
        self.varCustom = StringVar()
        #Label for the the option to add custom text
        self.lblCustom = Label(self.master, text='Custom text or click the Default HTML page button', font = ("Arial, 12"))
        self.lblCustom.grid(row=0, column=0, padx=(10,0), pady=(10,0))
        #Entry location for the custom text
        self.txtCustom = Entry(self.master, text='', width=50, font = ("Arial, 12"))
        self.txtCustom.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
        

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "<html>\n<body>\n<h1>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #Puts the custom text entered as the header on html page
    def SubmitCustom(self):
        Cus = self.txtCustom.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + Cus + "<html>\n<body>\n<h1>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
