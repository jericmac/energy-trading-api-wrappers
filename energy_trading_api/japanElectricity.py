"""
Japan Electricity Utilities Web APIs

List of Utilities:
    - Kyushu Electric
    -
"""

import pandas as pd
from io import StringIO
import requests

def __call_api_kyushuElectric(endpoint, column_names=None, skiprows=7,nrows=24):
    url = f"http://www.kyuden.co.jp/power_usages/csv/juyo-hourly-{endpoint}.csv"
    s = StringIO(requests.get(url).content.decode("Shift JIS")) #Use Japanese encoding
    try:
        if column_names==None:
            return pd.read_csv(s, skiprows=skiprows,nrows=nrows)
        else:
            return pd.read_csv(s, header=None,skiprows=skiprows+1, nrows=nrows,names=column_names)
    except Exception as e:
        print(e)
        return None

def kyushuElectricdemandJapanese(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}")

def kyushuElectricdemandEnglish(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}",column_names=["date", "time", "actual demand 10,000 kW", "forecast 10,000 kW","Usage (%)"])

def kyushuElectricDemand5MSJapanese(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}",skiprows=42,nrows=288)

def kyushuElectricDemand5MSEnglish(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}",skiprows=42,nrows=288,column_names=["date","time","5-Minute Actuals 10,000 kW"])

