"""
Japan Federation of Electricity Power Companies Web APIs

"""

import pandas as pd
from io import StringIO
import requests


#region FEPC

def __call_api_FEPC_powerStatistics(endpoint,doubleHeader=False):
    url = f"https://raw.githubusercontent.com/jericmac/fepc_japan/main/Power%20Statistics/{endpoint}.csv"
    try:
        s = requests.get(url).content
        if (doubleHeader==False):
            df = pd.read_csv(StringIO(s.decode('utf-8')))
        else:
            df = pd.read_csv(StringIO(s.decode('utf-8')), header=[0, 1])
        return df
    except Exception as e:
        print(e)
        return None

def generationFacilityByCompany():
    endpoint = "1_1%20A%20Generation%20facility%20(by%20company%2C%20by%20power%20source)"
    return __call_api_FEPC_powerStatistics(endpoint)

def generationFacilityByServiceArea():
    endpoint = "1_2%20Generation%20facility%20(by%20service%20area)"
    return __call_api_FEPC_powerStatistics(endpoint)

def purchaseContracts():
    endpoint = "1_3%20Purchase%20Contracts"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def substationFacility():
    endpoint = "1_4%20Substation%20Facility"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def transmissionFacility():
    endpoint = "1_5%20Transmission%20Facility"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def electricityGeneratedAndPurchased():
    endpoint = "2_1%20M%20Electricity%20generated%20and%20purchased"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def demandWithOptionalSupplyProvisionsPre1999():
    endpoint = "2_10%20M%20Demand%20with%20Optional%20Supply%20Provisions%20Pre1999"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def numberOfCustomersForLightingAndPowerDemands():
    endpoint = "2_2%20M%20Number%20of%20Customers%20for%20Lighting%20and%20Power%20demands"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def contractedDemandsInLightingAndPowerSections():
    endpoint = "2_3%20M%20Contracted%20demands%20(kW)%20in%20Lighting%20and%20Power%20sections"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def electricityConsumedInLightingAndPowerSections():
    endpoint = "2_4%20M%20Electricity%20consumed%20in%20Lighting%20and%20Power%20sections"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def electricityConsumedByIndustry():
    endpoint = "2_5%20M%20Electricity%20consumed%20(by%20industry)"
    return __call_api_FEPC_powerStatistics(endpoint,True)


def electricityLossRate():
    endpoint = "2_6%20M%20Electricity%20Loss%20Rate"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def fuelTrackRecord():
    endpoint = "2_7%20H%20Fuel%20Track%20Record"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def hydroelectricFlowRate():
    endpoint = "2_8%20M%20Flow%20Rate%20of%20Hydroelectric"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def maximumPeakLoad():
    endpoint = "2_9%20M%20Maximum%20Peak%20Load"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def earningsSummary():
    endpoint = "3_1%20A%20Earnings%20Summary"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def balanceSheetAssets():
    endpoint = "3_2%20A%20Balance%20Sheet%20(Assets)"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def balanceSheetLiabilityAndEquity():
    endpoint = "3_3%20A%20Balance%20Sheet%20(Liability%20and%20Equity)"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def profitAndLoss():
    endpoint = "3_4%20A%20Profit%20and%20Loss"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def fundRaisingTrackRecord():
    endpoint = "4_1%20A%20Fund-Raising%20Track%20Record"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def demandByUse():
    endpoint = "5_1%20M%20Demand%20By%20Use"
    return __call_api_FEPC_powerStatistics(endpoint,True)

def demandByIndustry():
    endpoint = "6_1%20M%20Demand%20(By%20Industry)"
    return __call_api_FEPC_powerStatistics(endpoint,True)

#endregion FEPC