import pandas as pd
from datetime import datetime
import pickle, os, requests


def quit_action(app):
    """
    Store user's data in pickle form on their device. Also send close signal.
    """
    try:
        app.n
        app.n.close_app(app.emailVar.get(), app.emailVar2.get(), app.groupIdListVar.get())
    except:
        pass

    if app.rememberMeVar.get() == 1:
        if app.userEmailVar.get() != '':
            data = {
                app.userEmailVar.get(): {
                    'email':app.emailVar.get(), 'pass':app.passVar.get(), 'teleId':app.teleIdVar.get(),
                    'keywords':app.keywordsVar.get(), 'blacklistKeywords':app.blacklistKeywordsVar.get(),
                    'email2':app.emailVar2.get(), 'pass2':app.passVar2.get(), 'teleId2':app.teleIdVar2.get(),
                    'keywords2':app.keywordsVar2.get(), 'blacklistKeywords2':app.blacklistKeywordsVar2.get(),
                    'groupIdList':app.groupIdListVar.get()
                }
            }

            if os.path.exists('info'):
                with open('info', 'rb') as f:
                    obj = pickle.load(f)
                obj.update(data)
                with open('info', 'wb') as f:
                    pickle.dump(obj, f)

            else:
                with open('info', 'wb') as f:
                    pickle.dump(data, f)