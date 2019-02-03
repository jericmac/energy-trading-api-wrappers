"""
Japan Electric Power eXchange (JEPX)
Website - www.jepx.org
API Details - Day-ahead Spot prices and Trading Volumes over 48 Trading Intervals

Dataset:
Column 1: Date in YYYY/MM/DD format
Column 2: Trading interval (1-48)
Column 3: Price in JPY/kWh
Column 4: Volume in MWh

Usage: call "spotLatest", providing date in YYYYMMDD format. Will otherwise return the latest day-ahead data.


"""

import pandas as pd
import io
import requests

def __call_api(endpoint):
    url="http://www.jepx.org/data/%s"%(endpoint)
    s = requests.get(url).content
    try:
        results = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None,names = ["date", "interval", "price", "volume"])
    except:
        results = None

    return results

def spotLatest(day=None):

    if day is None:
        endpoint = 'SpotLatest.csv'
    elif day is not None:
        endpoint = """{0}.csv""".format(day)

    result = __call_api(endpoint)

    return result


