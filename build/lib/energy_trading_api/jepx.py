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


def __call_api(endpoint, column_names=None):
    url = f"http://www.jepx.org/data/{endpoint}"
    s = StringIO(requests.get(url).content.decode("utf-8"))
    try:
        return pd.read_csv(s, header=None, names=column_names)
    except:
        return None


def spotLatest(day="SpotLatest"):
    return __call_api(
        f"{day}.csv", column_names=["date", "interval", "price", "volume"]
    )

