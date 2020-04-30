import tkinter as tk
from tkinter import ttk
from network import Network
import pickle

class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        ## Top Frame
        mainFrame = tk.Frame(self, pady=35)

        # Email Row
        emailLabel = tk.Label(mainFrame, text='User Email')
        emailLabel.grid(row=2, sticky='E')

        self.emailEntry = tk.Entry(mainFrame, textvariable=self.controller.userEmailVar)
        self.emailEntry.grid(row=2, column=1, ipadx=30, padx=5, pady=2)

        # Password Row
        passLabel = tk.Label(mainFrame, text='User Password')
        passLabel.grid(row=3, sticky='E')

        self.passEntry = tk.Entry(mainFrame, textvariable=self.controller.userPasswordVar, show='*')
        self.passEntry.grid(row=3, column=1, ipadx=30)

        # Remember Me Button
        RememberBtn = tk.Checkbutton(mainFrame, text='Save Settings', variable=self.controller.rememberMeVar)
        RememberBtn.grid(columnspan=2)
        
        # Login Button
        LoginBtn = ttk.Button(mainFrame, text='Login', command=self.loginAction)
        LoginBtn.grid(row=6, columnspan=2, ipadx=5, ipady=5, pady=10)
        mainFrame.pack()


    def loginAction(self):
        self.controller.n = Network(self.emailEntry.get(), self.passEntry.get(), self.controller)
        r = self.controller.n.login()
        self.controller.statusBar['text'] = r

        if r == 'Login Successfully':
            self.load_info()
            self.controller.n.ping()
            self.lower()
        else:
            del self.controller.n
            self.controller.statusBarLogin['text'] = r


    def load_info(self):
        try:
            with open('info', 'rb') as f:
                self.controller.defaultVar = pickle.load(f)
            if self.emailEntry.get() not in self.controller.defaultVar:
                raise Exception
        except:
            self.controller.defaultVar = {
                self.emailEntry.get(): {
                    'email':'', 'pass':'', 'teleId':'', 'keywords':'', 'blacklistKeywords':'',
                    'email2':'', 'pass2':'', 'teleId2':'', 'keywords2':'', 'blacklistKeywords2':'', 'groupIdList':''
                }
            }

        self.controller.emailVar.set(self.controller.defaultVar[self.emailEntry.get()]['email'])
        self.controller.passVar.set(self.controller.defaultVar[self.emailEntry.get()]['pass'])
        self.controller.teleIdVar.set(self.controller.defaultVar[self.emailEntry.get()]['teleId'])
        self.controller.keywordsVar.set(self.controller.defaultVar[self.emailEntry.get()]['keywords'])
        self.controller.blacklistKeywordsVar.set(self.controller.defaultVar[self.emailEntry.get()]['blacklistKeywords'])

        self.controller.emailVar2.set(self.controller.defaultVar[self.emailEntry.get()]['email2'])
        self.controller.passVar2.set(self.controller.defaultVar[self.emailEntry.get()]['pass2'])
        self.controller.teleIdVar2.set(self.controller.defaultVar[self.emailEntry.get()]['teleId2'])
        self.controller.keywordsVar2.set(self.controller.defaultVar[self.emailEntry.get()]['keywords2'])
        self.controller.blacklistKeywordsVar2.set(self.controller.defaultVar[self.emailEntry.get()]['blacklistKeywords2'])
        self.controller.groupIdListVar.set(self.controller.defaultVar[self.emailEntry.get()]['groupIdList'])