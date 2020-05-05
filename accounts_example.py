import requests
import json

spreadsheetId = ''
apiKey = ''
_range = ''

url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{_range}?key={apiKey}'

def get_url():
    """
    Domain will be changed after time, so client need to fetch latest domain
    """
    r = requests.get(url)
    domain = 'https://{}.localhost.run'.format(json.loads(r.content.decode())['values'][0][0])
    return domain
