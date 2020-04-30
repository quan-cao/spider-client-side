import requests
import json

spreadsheetId = '1zEZl0Do3jiWNsT03sdicwYeCP11rOe1m-Wv66URG-xM'
apiKey = 'AIzaSyAzr3ZV-eJ58M-VJmACMZWDr-Mu_twqflA'
_range = 'A2'

url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{_range}?key={apiKey}'

def get_url():
    """
    Domain will be changed after time, so client need to fetch latest domain
    """
    r = requests.get(url)
    domain = 'https://{}.localhost.run'.format(json.loads(r.content.decode())['values'][0][0])
    return domain
