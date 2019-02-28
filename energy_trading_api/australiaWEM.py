"""
Western Australia Wholesale Electricity Market (WEM) Web APIs

An API Wrapper for the reports found in the WEM Data website:
    http://data.wa.aemo.com.au

    -Participants
    -Facilities
    -Comissioning Tests
    -Load Forecast
    -Extended Load Forecast
    -Historical Load Forecast
    -Non Balancing Dispatch Merit Order
    -Demand SIde Programme Prices
    -Operational Measurements
    -Facility SCADA
    -Load Summary
    -Outages
    -IRCR Ratios
    -Peak SWIS Trading Intervals
    -Real Time Outages
    -Refund Exempt Planned Outage
    -Real Time Dispatch Advisories
    -Market Advisories
    -Balancing Market Summary
    -Effective Balancing Submission
    -STEM Summary
    -STEM Participant Activity
    -STEM Bids and Offers
    -STEM Facility Declarations

"""

import pandas as pd
from io import StringIO
import requests
import datetime

def __call_api(endpoint, ignore_errors=False,low_memory=True):
    url = f"http://data.wa.aemo.com.au/datafiles/{endpoint}"
    try:
        if ignore_errors==False:
            s = StringIO(requests.get(url).content.decode("utf-8"))
        else:
            s = StringIO(requests.get(url).content.decode("utf-8","ignore"))

        if low_memory==True:
            return pd.read_csv(s)
        else:
            return pd.read_csv(s,low_memory=False)
    except Exception as e:
        print(e)
        return None

def participants():
    return __call_api(endpoint=f"participants/participants.csv")

def facilities():
    return __call_api(endpoint=f"facilities/facilities.csv")

def commissioningTest(year="2019"):
    return __call_api(endpoint=f"commissioning-test/commissioning-test-summary-{year}.csv")

def loadForecast():
    return __call_api(endpoint=f"load-forecast/load-forecast.csv")

def extendedLoadForecast():
    return __call_api(endpoint=f"extended-load-forecast/extended-load-forecast.csv")

def historicalLoadForecast(year="2019"):
    return __call_api(endpoint=f"historical-load-forecast/historical-load-forecast-{year}.csv")

def nonbalancingDispatchMeritOrder(yearmonth="2019-01"):
    return __call_api(endpoint=f"non-balancing-dispatch-merit-order/nbdmo-{yearmonth}.csv")

def demandSideProgrammePrices(year="2019"):
    return __call_api(endpoint=f"dsp-decrease-price/dsp-decrease-price-{year}.csv")

def operationalMeasurements(year="2019"):
    return __call_api(endpoint=f"operational-measurements/operational-measurements-{year}.csv")

def facilitySCADA(yearmonth="2019-01"):
    return __call_api(endpoint=f"facility-scada/facility-scada-{yearmonth}.csv",low_memory=False)

def loadSummary(year="2018"):
    return __call_api(endpoint=f"load-summary/load-summary-{year}.csv")

def outages(year="2019"):
    return __call_api(endpoint=f"outages/outages-{year}.csv",low_memory=False)

def ircrRatios():
    return __call_api(endpoint=f"ircr-ratios/ircr-ratios.csv")

def peakSWISIntervals():
    return __call_api(endpoint=f"peak-intervals/peak-intervals.csv")

def realTimeOutages():
    return __call_api(endpoint=f"realtime-outages/realtime-outages.csv",ignore_errors=True)

#REPO = refund exempt planned outage count
def repoCount():
    return __call_api(endpoint=f"repo-count/repo-count.csv")

def dispatchAdvisory():
    return __call_api(endpoint=f"dispatch-advisory/dispatch-advisory.csv",ignore_errors=True)

def marketAdvisory():
    return __call_api(endpoint=f"market-advisory/market-advisory.csv")

def balancingSummary(year="2019"):
    return __call_api(endpoint=f"balancing-summary/balancing-summary-{year}.csv")

def effectiveBalancingSubmission(yearmonth="2019-01"):
    return __call_api(endpoint=f"effective-balancing-submission/effective-balancing-submission-{yearmonth}.csv",low_memory=False)

def stemSummary(year="2019"):
    return __call_api(endpoint=f"stem-summary/stem-summary-{year}.csv")

def stemParticipantActivity(yearmonth="2019-01"):
    return __call_api(endpoint=f"stem-participant-activity/stem-participant-activity-{yearmonth}.csv")

def stemBidsAndOffers(yearmonth="2019-01"):
    return __call_api(endpoint=f"stem-bids-and-offers/stem-bids-and-offers-{yearmonth}.csv",low_memory=False)

def stemFacilityDeclarations(yearmonth="2019-01"):
    return __call_api(endpoint=f"stem-facility-declarations/stem-facility-declarations-{yearmonth}.csv",low_memory=False)
