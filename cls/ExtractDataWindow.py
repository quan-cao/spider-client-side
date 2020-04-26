import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import filedialog, messagebox
import threading, os, json, datetime
import pandas as pd

class ExtractDataWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.dirToSave = os.getcwd()

        self.mainFrame = ttk.Frame(self.parent)

        timeFrame = tk.Frame(self.mainFrame, pady=3)
        fromTimeLbl = ttk.Label(timeFrame, text='From time')
        fromTimeLbl.grid(sticky='E', padx=2)
        self.fromTimeEntry = DateEntry(timeFrame, date_pattern='y-mm-dd')
        self.fromTimeEntry.grid(row=0, column=1, padx=2)
        toTimeLbl = ttk.Label(timeFrame, text='To time')
        toTimeLbl.grid(sticky='E', row=0, column=2, padx=2)
        self.toTimeEntry = DateEntry(timeFrame, date_pattern='y-mm-dd')
        self.toTimeEntry.grid(row=0, column=3, padx=2)
        timeFrame.pack()

        fileFrame = tk.Frame(self.mainFrame, pady=3)
        fileNameLbl = ttk.Label(fileFrame, text='File name')
        fileNameLbl.grid(row=0, column=0, padx=2)
        self.fileNameEntry = ttk.Entry(fileFrame)
        self.fileNameEntry.grid(row=0, column=1, padx=2, ipadx=60, sticky='ew')
        fileFrame.pack()

        buttonFrame = tk.Frame(self.mainFrame, pady=3)
        dirBtn = ttk.Button(buttonFrame, text='Choose where to save files', command=self.chooseDir)
        dirBtn.grid(row=0, columnspan=2, pady=5)
        getAdsPostBtn = ttk.Button(buttonFrame, text='Get Ads Posts', command=self.extract_ads_posts)
        getAdsPostBtn.grid(row=1, column=0, padx=4)
        GetGroupPostsBtnbtn = ttk.Button(buttonFrame, text='Get Group Posts', command=self.extract_groups_posts)
        GetGroupPostsBtnbtn.grid(row=1, column=1, padx=4)
        buttonFrame.pack()

        self.mainFrame.pack(fill='x')

    def extract_ads_posts(self):
        try:
            self.controller.n
        except:
            messagebox.showinfo(title='Invalid Credentials', message='Please log-in.')
            return None
            
        if self.fileNameEntry.get() == '':
            messagebox.showinfo(title='Missing Information', message='Please fill file name.')

        else:
            try:
                if (self.controller.timeExtract + datetime.timedelta(seconds=30)) > datetime.datetime.now():
                    waitTime = ((self.controller.timeExtract + datetime.timedelta(seconds=30)) - datetime.datetime.now()).seconds
                    if waitTime > 0:
                        self.controller.statusBar['text'] = 'Please wait for {} seconds'.format(str(waitTime))
                        return None
                    else:
                        del self.controller.timeExtract
                        del waitTime
            except:
                pass
            self.controller.statusBar['text'] = 'Extracting Ads Data...'
            data = self.controller.n.extract_posts('ads', self.fromTimeEntry.get(), self.toTimeEntry.get())
            if data.find('[') != -1:
                data = json.loads(data)
                df = pd.json_normalize(data)
                df.to_excel(f"{self.dirToSave}\\{self.fileNameEntry.get()}.xlsx", index=False)
                self.controller.statusBar['text'] = 'Extracted data at {}'.format(self.dirToSave)
            else:
                self.controller.statusBar['text'] = data
            self.controller.timeExtract = datetime.datetime.now()

    def extract_groups_posts(self):
        try:
            self.controller.n
        except:
            messagebox.showinfo(title='Invalid Credentials', message='Please log-in.')
            return None
            
        if self.fileNameEntry.get() == '':
            messagebox.showinfo(title='Missing Information', message='Please fill file name.')

        else:
            try:
                if (self.controller.timeExtract + datetime.timedelta(seconds=30)) > datetime.datetime.now():
                    waitTime = ((self.controller.timeExtract + datetime.timedelta(seconds=30)) - datetime.datetime.now()).seconds
                    if waitTime > 0:
                        self.controller.statusBar['text'] = 'Please wait for {} seconds'.format(str(waitTime))
                        return None
                    else:
                        del self.controller.timeExtract
                        del waitTime
            except:
                pass
            self.controller.statusBar['text'] = 'Extracting Groups Data...'
            data = self.controller.n.extract_posts('groups', self.fromTimeEntry.get(), self.toTimeEntry.get())
            if data.find('[') != -1:
                data = json.loads(data)
                df = pd.json_normalize(data)
                df.to_excel(f"{self.dirToSave}\\{self.fileNameEntry.get()}.xlsx", index=False)
                self.controller.statusBar['text'] = 'Extracted data at {}'.format(self.dirToSave)
            else:
                self.controller.statusBar['text'] = data
            self.controller.timeExtract = datetime.datetime.now()

    def chooseDir(self):
        self.dirToSave = filedialog.askdirectory()
        self.mainFrame.focus()