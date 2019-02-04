"""
U.S. Energy Information Administration
This is an API wrapper  for the eia-python API wrapper.

Contains select calls to distinct Data Series, and returns pandas dataFrames

"""
import eia
import pandas as pd
from .common import commonData


def __call_api(report,key="",series=None):
    api = eia.API(key)
    if series==None:
        series_search = api.data_by_series(series=commonData.dictEiaReports.get(report))
    else:
        series_search = api.data_by_series(series=series)

    result = pd.DataFrame(series_search)
    return result

def eiaAPI(seriesID="",key=""):
    return __call_api(report = None,key =key,series=seriesID)

def coalAustraliaProduction(key=""):
    return __call_api(report="australiaCoalProduction",key=key,series=None)

def coalAustraliaConsumption(key=""):
    return __call_api(report="australiaCoalConsumption",key=key,series=None)

def ngAustraliaProduction(key=""):
    return __call_api(report="australiaNGConsumption",key=key,series=None)

def ngHenryHubSpotDaily(key=""):
    return __call_api(report="henryHubNGSpotPriceDaily",key=key,series=None)

def crudeCushingSpotDaily(key=""):
    return __call_api(report="wtiCushingSpotPriceDaily",key=key,series=None)


