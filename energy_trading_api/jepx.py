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
from io import StringIO
import requests
from .common import combineTimePeriodDate
from .common import mappingJEPX

def __call_api(endpoint, column_names=None,encoding="utf-8"):
    url = f"http://www.jepx.org/{endpoint}"
    s = StringIO(requests.get(url).content.decode(encoding))
    try:
        if column_names==None:
            return pd.read_csv(s, header=None)
        else:
            return pd.read_csv(s, header=None, names=column_names)
    except:
        return None


def spotLatest(day="SpotLatest"):
    return __call_api(
        f"data/{day}.csv", column_names=["date", "interval", "price", "volume"]
    )

def spotHistorical(year="2019"):
    endpoint =f"market/excel/spot_{year}.csv"
    dfRecords = __call_api(endpoint,encoding="Shift JIS")
    dfRecords = dfRecords[1:]
    dfRecords.rename(columns=mappingJEPX, inplace=True)
    dfRecords = combineTimePeriodDate(dF=dfRecords, targetColumn='DATETIME', periodColumn='PERIOD', targetColumnFmt='%Y/%m/%d')
    return dfRecords




