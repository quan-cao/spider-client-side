import tkinter as tk
from utils.texts import *
from tkinter import messagebox
from cls.ExtractDataWindow import ExtractDataWindow
from cls.ChangePasswordWindow import ChangePasswordWindow

class MenuBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        menu = tk.Menu()

        helpMenu = tk.Menu(menu, tearoff=0)
        fileMenu = tk.Menu(menu, tearoff=0)

        menu.add_cascade(label='File', menu=fileMenu)
        menu.add_cascade(label='Help', menu=helpMenu)

        helpMenu.add_command(label='Manual', command=self.add_manual)
        helpMenu.add_separator()
        helpMenu.add_command(label='About', command=self.add_about)

        fileMenu.add_command(label='Extract data', command=self.addExtractDataWindow)
        fileMenu.add_separator()
        fileMenu.add_command(label='Change Password', command=self.addChangePasswordWindow)

        self.controller.config(menu=menu)

    def add_manual(self):
        try:
            if self.manualWindow.state() == 'normal':
                self.manualWindow.focus()
        except:
            self.manualWindow = tk.Toplevel(self.parent)
            self.manualWindow.title('Manual')
            self.manualWindow.geometry("800x610")
            self.manualWindow.resizable(0,0)
            manualFrame = tk.Frame(self.manualWindow)
            manualTxt = tk.Text(manualFrame, wrap='word', padx=20, pady=5, spacing1=8, bd=3, bg='#ededed', relief='flat')
            manualTxt.insert('insert', manualText)
            manualTxt.configure(state='disabled', font=("Rouge", 10))
            manualTxt.pack(fill='both', expand=True)
            manualFrame.pack(fill='both', expand=True)

    def add_about(self):
        messagebox.showinfo(title='About', message=aboutText)

    def addExtractDataWindow(self):
        try:
            if self.popUpExtract.state() == 'normal':
                self.popUpExtract.focus()
        except:
            self.popUpExtract = tk.Toplevel(self.controller)
            self.popUpExtract.title('Extract Data')
            self.popUpExtract.resizable(0,0)
            windowsExtract = ExtractDataWindow(self.popUpExtract, self.controller)

    def addChangePasswordWindow(self):
        try:
            if self.popUpChangePass.state() == 'normal':
                self.popUpChangePass.focus()
        except:
            self.popUpChangePass = tk.Toplevel(self.controller)
            self.popUpChangePass.title('Change Password')
            self.popUpChangePass.resizable(0,0)
            windowsChangePass = ChangePasswordWindow(self.popUpChangePass, self.controller)