"""WA Gas Bulletin Board API Wrapper
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize


def __call_api(endpoint):
    return requests.get(f"https://gbbwa.aemo.com.au/api/v1/report/{endpoint}").json()


def _basic_gasday_call(endpoint, gasDay="current", record_prefix=None, column_pop=None):
    result = __call_api(f"{endpoint}/{gasDay}")

    df = pd.io.json.json_normalize(
        result, ["rows"], ["reportId", "asAt", "gasDay"], record_prefix=record_prefix
    )
    if column_pop:
        # The result comes with the Capacity column structured as a dict, so this next line breaks it up to columns
        return df.join(pd.DataFrame(df.pop(column_pop).tolist()))
    return df

def actualFlow(gasDay="current", month=None):
    return _basic_gasday_call("actualFlow", gasDay)


def endUserConsumption(gasDay="current"):
    return _basic_gasday_call("endUserConsumption", gasDay)


def largeUserConsumptionByCategory(gasDay="current"):
    return _basic_gasday_call("largeUserConsumptionByCategory", gasDay)

def mediumTermCapacity(gasDay="current"):
    return _basic_gasday_call("mediumTermCapacity", gasDay)


def gasSpecification(gasDay="current"):
    return _basic_gasday_call("gasSpecification", gasDay, record_prefix="_")


def largeUserConsumption(gasDay="current"):
    return _basic_gasday_call("largeUserConsumption", gasDay, record_prefix="_")


def capacityOutlook(gasDay="current"):
    return _basic_gasday_call("capacityOutlook", gasDay, column_pop="capacity")


def linepackCapacityAdequacy(gasDay="current"):
    return _basic_gasday_call("linepackCapacityAdequacy", gasDay, column_pop="status")


def forecastFlow(gasDay="current"):

    dataFrame_rows = _basic_gasday_call("forecastFlow", gasDay, column_pop="forecast")

    for i in range(7):
        dataFrame_rows = dataFrame_rows.join(
            pd.DataFrame(dataFrame_rows.pop(f"d{i}").tolist())
        )
        dataFrame_rows.rename(
            columns={"delivery": f"d{i}_delivery", "receipt": f"d{i}_receipt"},
            inplace=True,
        )
    return dataFrame_rows
