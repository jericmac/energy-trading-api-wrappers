"""WA Gas Bulletin Board API Wrapper
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize

def __call_api(endpoint):
    request = requests.get('https://gbbwa.aemo.com.au/api/v1/report%s' %(endpoint))
    return request.json()


#region CAPACITY OUTLOOK REPORT
def capacityOutlook(gasDay=None):

    if gasDay is None:
        endpoint = '/capacityOutlook/current'
    elif gasDay is not None:
        endpoint = """/capacityOutlook/{0}""".format(gasDay)

    result = __call_api(endpoint)

    dataFrame_rows = pd.io.json.json_normalize(result, ['rows'],['reportId','asAt','gasDay'])
    # The result comes with the Capacity column structured as a dict, so this next line breaks it up to columns
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('capacity').tolist()))
    return dataFrame_rows

#endregion CAPACITY OUTLOOK REPORT

#region ACTUAL FLOWS

def actualFlow(gasDay=None,month=None):

    if gasDay is None and month is None:
        endpoint = '/actualFlow/current'
    elif gasDay is not None:
        endpoint = """/actualFlow/{0}""".format(gasDay)
    elif month is not None:
        None
        # TBA - the API returns a CSV file for monthly actuals
        # endpoint = """/actualFlow/{0}""".format(month)


    result = __call_api(endpoint)

    dataFrame_rows = pd.io.json.json_normalize(result, ['rows'],['reportId','asAt','gasDay'])

    return dataFrame_rows
#endregion

#region End User Consumption
def endUserConsumption(gasDay=None):

    if gasDay is None :
        endpoint = '/endUserConsumption/current'
    elif gasDay is not None:
        endpoint = """/endUserConsumption/{0}""".format(gasDay)
    result = __call_api(endpoint)
    dataFrame_rows = pd.io.json.json_normalize(result, ['rows'],['reportId','asAt','gasDay'])

    return dataFrame_rows
#endregion End User Consumption

#region forecast Flow (Nominations and FORECASTS)
def forecastFlow(gasDay=None):

    if gasDay is None :
        endpoint = '/forecastFlow/current'
    elif gasDay is not None:
        endpoint = """/forecastFlow/{0}""".format(gasDay)
    result = __call_api(endpoint)
    dataFrame_rows = pd.io.json.json_normalize(result, ['rows'],['reportId','asAt','gasDay'])
    # breakout daily forecast receipts and deliveries
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('forecast').tolist()))

    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d0').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd0_delivery', 'receipt': 'd0_receipt'},inplace=True)
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d1').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd1_delivery', 'receipt': 'd1_receipt'}, inplace=True)
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d2').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd2_delivery', 'receipt': 'd2_receipt'}, inplace=True)
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d3').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd3_delivery', 'receipt': 'd3_receipt'}, inplace=True)
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d4').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd4_delivery', 'receipt': 'd4_receipt'}, inplace=True)
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d5').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd5_delivery', 'receipt': 'd5_receipt'}, inplace=True)
    dataFrame_rows = dataFrame_rows.join(pd.DataFrame(dataFrame_rows.pop('d6').tolist()))
    dataFrame_rows.rename(columns={'delivery': 'd6_delivery', 'receipt': 'd6_receipt'}, inplace=True)
    return dataFrame_rows
#endregion forecast Flow

#region Gas Specification
def gasSpecification(gasDay=None):

    if gasDay is None :
        endpoint = '/gasSpecification/current'
    elif gasDay is not None:
        endpoint = """/gasSpecification/{0}""".format(gasDay)
    result = __call_api(endpoint)
    dataFrame_rows = pd.io.json.json_normalize(result, ['rows'],['reportId','asAt','gasDay'],record_prefix='_')

    return dataFrame_rows
#endregion Gas Specification

#region Large User Consumption
#endregion Large User Consumption

#region Large User Consumption by Category
#endregion Large User Consumption by Category

#region Linepack Capacity Adequacy
#endregion Linepack Capacity Adequacy

#region medium Term Capacity
#endregion medium Term Capacity


print(gasSpecification().to_string())