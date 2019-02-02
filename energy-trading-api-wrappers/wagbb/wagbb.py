import requests
import pandas as pd
from pandas.io.json import json_normalize


url_Report = 'https://gbbwa.aemo.com.au/api/v1/report/capacityOutlook/current'

r = requests.get(url_Report)
df = pd.io.json.json_normalize(r.json(),['rows'])
df1 = df.join(pd.DataFrame(df.pop('capacity').tolist()))

def __call_api(endpoint):
    request = requests.get('https://gbbwa.aemo.com.au/api/v1/report%s' %(endpoint))
    return request.json()

def capacityOutlook():
    result = __call_api('/capacityOutlook/current')
    df = pd.io.json.json_normalize(result, ['rows'])
    df1 = df.join(pd.DataFrame(df.pop('capacity').tolist()))
    print(df1.to_string())