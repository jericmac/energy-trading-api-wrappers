"""WA Gas Bulletin Board API Wrapper
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize

def __call_api(endpoint):
    request = requests.get('https://gbbwa.aemo.com.au/api/v1/report%s' %(endpoint))
    return request.json()

def capacityOutlook():
    result = __call_api('/capacityOutlook/current')

    dataFrame = pd.io.json.json_normalize(result, ['rows'])
    # The result comes with the Capacity column structured as a dict, so this next line breaks it up to columns
    dataFrame = dataFrame.join(pd.DataFrame(dataFrame.pop('capacity').tolist()))
    return dataFrame