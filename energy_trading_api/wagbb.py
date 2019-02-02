"""WA Gas Bulletin Board API Wrapper
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize

def __call_api(endpoint):
    request = requests.get('https://gbbwa.aemo.com.au/api/v1/report%s' %(endpoint))
    return request.json()

#region CAPACITY OUTLOOK REPORT

# blank call - current
def capacityOutlook(date=None):

    if date is None:
        endpoint = '/capacityOutlook/current'
    elif date is not None:
        endpoint = """/capacityOutlook/{0}""".format(date)

    result = __call_api(endpoint)

    dataFrame_rows = pd.io.json.json_normalize(result, ['rows'],['reportId','asAt','gasDay'])
    # The result comes with the Capacity column structured as a dict, so this next line breaks it up to columns
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('capacity').tolist()))
    return dataFrame_rows

#endregion CAPACITY OUTLOOK REPORT