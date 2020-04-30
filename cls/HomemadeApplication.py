import tkinter as tk
from tkinter import ttk

from cls import *


class HomemadeApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.iconbitmap(default='app-icon.ico')
        self.title("Spider")
        self.resizable(0,0)
        self.version = '0.1.0'
        self.connStatus = False

        self.userEmailVar = tk.StringVar()
        self.userPasswordVar = tk.StringVar()
        self.rememberMeVar = tk.IntVar()
        self.rememberMeVar.set(1)

        self.emailVar = tk.StringVar()
        self.passVar = tk.StringVar()
        self.teleIdVar = tk.StringVar()
        self.keywordsVar = tk.StringVar()
        self.blacklistKeywordsVar = tk.StringVar()

        self.emailVar2 = tk.StringVar()
        self.passVar2 = tk.StringVar()
        self.teleIdVar2 = tk.StringVar()
        self.keywordsVar2 = tk.StringVar()
        self.blacklistKeywordsVar2 = tk.StringVar()
        self.groupIdListVar = tk.StringVar()

        # Log-in Screen
        loginFrame = LoginWindow(self, self)
        loginFrame.grid(row=0, column=0, sticky='nsew')
        self.statusBarLogin = tk.Label(loginFrame, text='Please log in', bd=1, relief='sunken', anchor='w')
        self.statusBarLogin.pack(side='bottom', fill='x')

        # In App Screen
        inAppFrame = tk.Frame(self)
        menu = MenuBar(inAppFrame, self)
        tab_control = ttk.Notebook(inAppFrame)
        AdsPostsTab = AdsPostsWindow(tab_control, self)
        GroupPostsTab = GroupPostsWindow(tab_control, self)
        tab_control.add(AdsPostsTab, text='Ads Posts')
        tab_control.add(GroupPostsTab, text='Group Posts')
        tab_control.pack(expand=1, fill='both')
        self.statusBar = tk.Label(inAppFrame, bd=1, relief='sunken', anchor='w')
        self.statusBar.pack(side='bottom', fill='x')

        inAppFrame.grid(row=0, column=0)
        loginFrame.tkraise()