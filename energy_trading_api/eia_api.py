"""
U.S. Energy Information Administration
This is an API wrapper  for the eia-python API wrapper.

Contains select calls to distinct Data Series, and returns pandas dataFrames

"""
import eia
import pandas as pd
from .common import commonData


def __call_api(report,key):
    api = eia.API(key)
    series_search = api.data_by_series(series=commonData.dictEiaReports.get(report))
    result = pd.DataFrame(series_search)
    return result

def coalAustraliaProduction(key=""):
    return __call_api("australiaCoalProduction",key)


