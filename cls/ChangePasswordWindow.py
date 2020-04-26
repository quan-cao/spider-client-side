import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import threading, os, datetime
import pandas as pd

class ChangePasswordWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.dirToSave = os.getcwd()

        mainFrame = ttk.Frame(self.parent)

        oldPasswordLbl = ttk.Label(mainFrame, text='Old Password')
        oldPasswordLbl.grid(row=0, column=0, padx=2, pady=3)
        self.oldPasswordEntry = ttk.Entry(mainFrame, show='*')
        self.oldPasswordEntry.grid(row=0, column=1, padx=2, ipadx=60, sticky='ew')
        newPasswordLbl = ttk.Label(mainFrame, text='New Password')
        newPasswordLbl.grid(row=1, column=0, padx=2, pady=3)
        self.newPasswordEntry = ttk.Entry(mainFrame, show='*')
        self.newPasswordEntry.grid(row=1, column=1, padx=2, ipadx=60, sticky='ew')

        confirmPasswordLbl = ttk.Label(mainFrame, text='Confirm New Password')
        confirmPasswordLbl.grid(row=2, column=0, padx=2, pady=3)
        self.confirmPasswordEntry = ttk.Entry(mainFrame, show='*')
        self.confirmPasswordEntry.grid(row=2, column=1, padx=2, ipadx=60, sticky='ew')

        changeBtn = ttk.Button(mainFrame, text='Change Password', command=self.change_password)
        changeBtn.grid(columnspan=2, pady=3, ipadx=5, ipady=5)

        mainFrame.pack(fill='x')

    def change_password(self):
        try:
            self.controller.n
        except:
            messagebox.showinfo(title='Invalid Credentials', message='Please log-in.')
            return 'Invalid Credentials'

        if (self.oldPasswordEntry.get() != self.newPasswordEntry.get()) and (self.newPasswordEntry.get() == self.confirmPasswordEntry.get()):
            try:
                if (self.controller.timeChangePass + datetime.timedelta(seconds=5)) > datetime.datetime.now():
                    waitTime = ((self.controller.timeChangePass + datetime.timedelta(seconds=5)) - datetime.datetime.now()).seconds
                    if waitTime > 0:
                        self.controller.statusBar['text'] = 'Please wait for {} seconds'.format(str(waitTime))
                        return None
                    else:
                        del self.controller.timeChangePass
                        del waitTime
            except:
                pass
            r = self.controller.n.change_password(self.newPasswordEntry.get())
            self.controller.statusBar['text'] = r
            self.controller.timeChangePass = datetime.datetime.now()