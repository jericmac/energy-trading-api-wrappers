"""
Australian Renewable Energy API

    - REC Registry (https://www.rec-registry.gov.au/)

"""

import requests
import pandas as pd
from pandas.io.json import json_normalize

def __call_api(endpoint):
    return requests.get(f"https://www.rec-registry.gov.au/rec-registry/app/api/public-register/certificate-actions?date={endpoint}").json()


def _basic_rec_call(recDay):
    result = __call_api(recDay)

    df = pd.io.json.json_normalize(result,["result"],record_prefix=None)
    df.reset_index(level=0, inplace=True)
    rangeDF = df["certificateRanges"].apply(pd.Series)
    mergedDF = pd.concat([df.drop(['certificateRanges'], axis=1), rangeDF], axis=1)

    return mergedDF


def recDay(recDay):
    return _basic_rec_call(recDay = recDay)




