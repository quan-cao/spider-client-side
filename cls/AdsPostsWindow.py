import tkinter as tk
from tkinter import ttk
import threading
import datetime

class AdsPostsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ## Top Frame
        topFrame = tk.Frame(self, pady=10)

        # Email Row
        emailLabel = tk.Label(topFrame, text='Facebook Email/Phone')
        emailLabel.grid(row=0, sticky='E')

        emailEntry = tk.Entry(topFrame, textvariable=self.controller.emailVar)
        emailEntry.grid(row=0, column=1, ipadx=15, padx=5)

        # Password Row
        passLabel = tk.Label(topFrame, text='Facebook Password')
        passLabel.grid(row=1, sticky='E')

        passEntry = tk.Entry(topFrame, textvariable=controller.passVar, show='*')
        passEntry.grid(row=1, column=1, ipadx=15)

        # Telegram ID Row
        teleIdLabel = tk.Label(topFrame, text='Telegram User ID')
        teleIdLabel.grid(row=2, sticky='E')

        teleIdEntry = tk.Entry(topFrame, textvariable=controller.teleIdVar)
        teleIdEntry.grid(row=2, column=1, ipadx=15)

        # Remember Me Checkbox
        blankLine = tk.Label(topFrame)
        blankLine.grid(columnspan=2)

        # Keywords Row
        keywordsLabel = tk.Label(topFrame, text='Keywords')
        keywordsLabel.grid(row=4, sticky='E')

        keywordsEntry = tk.Entry(topFrame, textvariable=controller.keywordsVar)
        keywordsEntry.grid(row=4, column=1, ipadx=15)

        # Blacklist Keywords Row
        blacklistKeywordsLabel = tk.Label(topFrame, text='Blacklist Keywords')
        blacklistKeywordsLabel.grid(row=5, sticky='E')

        blacklistKeywordsEntry = tk.Entry(topFrame, textvariable=controller.blacklistKeywordsVar)
        blacklistKeywordsEntry.grid(row=5, column=1, ipadx=15)

        topFrame.pack()
        ## End Top Frame

        ## Lower Frame
        lowerFrame = tk.Frame(self)

        # Scraping Button
        stopBtn = ttk.Button(lowerFrame, text='Stop Scraping Ads', command=self.stop_scrape_ads)
        stopBtn.grid(row=0, column=0, ipadx=5, ipady=5)

        startBtn = ttk.Button(lowerFrame, text='Start Scraping Ads', command=self.start_scrape_ads)
        startBtn.grid(row=0, column=1, ipadx=5, ipady=5)

        lowerFrame.pack()

    def start_scrape_ads(self):
        self.controller.statusBar['text'] = 'Connecting...'
        r = self.controller.n.scrape_ads(self.controller.emailVar.get(), self.controller.passVar.get(), self.controller.teleIdVar.get(),
                                        self.controller.keywordsVar.get(), self.controller.blacklistKeywordsVar.get())
        self.countDownAds = datetime.datetime.now()
        self.controller.statusBar['text'] = r

    def stop_scrape_ads(self):
        if self.controller.n.scrapeAds == True:
            try:
                countDown = datetime.datetime.now() - self.countDownAds
            except:
                self.controller.statusBar['text'] = 'Nothing to stop'
                return None

            if countDown > datetime.timedelta(seconds=10):
                self.controller.statusBar['text'] = 'Stopping...'
                r = self.controller.n.stop('ads', self.controller.emailVar.get())
                self.controller.statusBar['text'] = r

            else:
                waitTime = ((self.countDownAds + datetime.timedelta(seconds=10)) - datetime.datetime.now()).seconds
                self.controller.statusBar['text'] = 'Too fast, please wait for {} seconds'.format(str(waitTime))
        else:
            self.controller.statusBar['text'] = 'Nothing to stop'