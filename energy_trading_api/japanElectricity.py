"""
Japan Electricity Utilities Web APIs

List of Utilities:
    - Kyushu Electric
    - Chubu Electric
"""

import pandas as pd
from io import StringIO
import requests
import datetime

#region Kyuden
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

def kyushuElectricDemandJapanese(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}")

def kyushuElectricDemandEnglish(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}",column_names=["date", "time", "actual demand 10,000 kW", "forecast 10,000 kW","Usage (%)"])

def kyushuElectricDemand5MSJapanese(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}",skiprows=42,nrows=288)

def kyushuElectricDemand5MSEnglish(day="20190101"):
    return __call_api_kyushuElectric(endpoint=f"{day}",skiprows=42,nrows=288,column_names=["date","time","5-Minute Actuals 10,000 kW"])

#endregion Kyuden

#region Chuden
def __call_api_chubuElectric(column_names=None, skiprows=0):
    url = f"http://denki-yoho.chuden.jp/denki_yoho_content_data/areajuyo_current.csv"
    s = StringIO(requests.get(url).content.decode("Shift JIS")) #Use Japanese encoding
    try:
        if column_names==None:
            return pd.read_csv(s, skiprows=skiprows)
        else:
            return pd.read_csv(s, header=None,skiprows=skiprows+1,names=column_names)
    except Exception as e:
        print(e)
        return None

def chubuElectricDemandJapanese():
    return __call_api_chubuElectric()

def chubuElectricDemandEnglish():
    return __call_api_chubuElectric(column_names=['DATE','Time',"Actual Demand 10,000 kW"])

def chubuElectricDemandJapaneseRange(begtime = "20180101",endtime="20180201"):
    df = __call_api_chubuElectric()
    df.set_index('DATE', inplace=True)
    begtime = datetime.datetime.strptime(begtime, '%Y%m%d')
    endtime = datetime.datetime.strptime(endtime, '%Y%m%d')
    return df.loc[begtime.strftime('%Y/%m/%d'):endtime.strftime('%Y/%m/%d')]

def chubuElectricDemandEnglishRange(begtime = "20180101",endtime="20180201"):
    df = __call_api_chubuElectric(column_names=['DATE','Time',"Actual Demand 10,000 kW"])
    df.set_index('DATE', inplace=True)
    begtime = datetime.datetime.strptime(begtime, '%Y%m%d')
    endtime = datetime.datetime.strptime(endtime, '%Y%m%d')
    return df.loc[begtime.strftime('%Y/%m/%d'):endtime.strftime('%Y/%m/%d')]

#endregion Chuden

#region TEPCO
def __call_api_TEPCO(endpoint, column_names=None, skiprows=7,nrows=24):
    url =f"http://www.tepco.co.jp/forecast/html/images/juyo-{endpoint}.csv"
    s = StringIO(requests.get(url).content.decode("Shift JIS"))  # Use Japanese encoding
    try:
        if column_names == None:
            return pd.read_csv(s, skiprows=skiprows, nrows=nrows)
        else:
            return pd.read_csv(s, header=None, skiprows=skiprows + 1, nrows=nrows, names=column_names)
    except Exception as e:
        print(e)
        return None

def tepcoElectricDemandHistoricalJapanese(year="2019"):
    return __call_api_TEPCO(endpoint=f"{year}",skiprows=2,nrows=9000)

def tepcoElectricDemandHistoricalEnglish(year="2019"):
    return __call_api_TEPCO(endpoint=f"{year}",skiprows=2,nrows=9000,column_names=["date", "time", "actual demand 10,000 kW"])

def tepcoElectricDemandCurrentJapanese():
    return __call_api_TEPCO(endpoint=f"j")

def tepcoElectricDemandCurrentEnglish():
    return __call_api_TEPCO(endpoint=f"j",column_names=["date", "time", "actual demand 10,000 kW","forecast 10,000 kW","Usage (%)"])

#endregion TEPCO

