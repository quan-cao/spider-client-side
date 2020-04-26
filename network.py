import requests, time, threading, json
from accounts import *


class Network:
    def __init__(self, email, password, app):
        self.email = email
        self.password = password
        self.app = app

        self.scrapeAds = False
        self.scrapeGroups = False
        self.url = apiUrl.format(self.app.requiredString.get())

    def ping_action(self):
        while True:
            try:
                requests.get(f'{self.url}/ping', data={'email':self.email}).json()
                time.sleep(15)
            except:
                self.app.statusBar['text'] = 'Disconnected'
                break


    def ping(self):
        threading.Thread(target=self.ping_action, daemon=True).start()


    def login(self):
        try:
            r = requests.get(f'{self.url}/login', data={'email':self.email, 'password':self.password, 'version':self.app.version}).json()
            self.token = r['token']
            if self.token:
                threading.Thread(target=self.ping).start()
                return 'Login Successfully'
            else:
                return r['message']
        except:
            return 'Cannot Connect To Server'


    def scrape_ads(self, fb_email, fb_pass, teleId, keywords, blacklistKeywords):
        if self.token and self.scrapeAds == False:
            self.scrapeAds = True
            try:
                r = requests.post(f'{self.url}/api/scrape-ads', data={'email':self.email, 'token':self.token, 'fb_email':fb_email, 'fb_pass':fb_pass,
                                                                'teleId':teleId, 'keywords':keywords, 'blacklistKeywords':blacklistKeywords}).json()
                return r['message']
            except:
                self.scrapeAds = False
                return 'Request Failed'
        elif self.scrapeAds == True:
            return 'Session Existed'


    def scrape_groups(self, fb_email, fb_pass, teleId, keywords, blacklistKeywords, groupIdList):
        if self.token and self.scrapeGroups == False:
            self.scrapeGroups = True
            r = requests.post(f'{self.url}/api/scrape-groups', data={'email':self.email, 'token':self.token, 'fb_email':fb_email, 'fb_pass':fb_pass,
                                                                'teleId':teleId, 'keywords':keywords, 'blacklistKeywords':blacklistKeywords,
                                                                'groupIdList':groupIdList}).json()
            return r['message']
        elif self.scrapeGroups == True:
            return 'Session Existed'


    def stop(self, _type, fb_email):
        if _type == 'ads':
            if self.scrapeAds == True:
                self.scrapeAds = False
                r = requests.post(f'{self.url}/api/stop-scrape', data={'email':self.email, 'token':self.token, 'fb_email':fb_email, 'fb_email2':'', 'type':_type}).json()
            else:
                return 'Stopped Scraping Ads'
        elif _type == 'groups':
            if self.scrapeGroups == True:
                self.scrapeGroups = False
                r = requests.post(f'{self.url}/api/stop-scrape', data={'email':self.email, 'token':self.token, 'fb_email':'', 'fb_email2':fb_email, 'type':_type}).json()
            else:
                return 'Stopped Scraping Groups'
        else:
            pass
        return r['message']


    def close_app(self, fb_email, fb_email2, group_id_list):
        r = requests.post(f'{self.url}/close-app', data={'email':self.email, 'token':self.token, 'fb_email':fb_email, 'fb_email2':fb_email2, 'group_id_list':group_id_list})


    def extract_posts(self, _type, fromTime, toTime):
        """
        Returns a DataFrame
        """
        r = requests.get(f'{self.url}/api/extract-posts', data={'email':self.email, 'token':self.token, 'type':_type, 'fromTime':fromTime, 'toTime':toTime}).json()
        return r['message']


    def change_password(self, newPassword):
        r = requests.put(f'{self.url}/change-password', data={'email':self.email, 'token':self.token, 'newPassword':newPassword}).json()
        return r['message']