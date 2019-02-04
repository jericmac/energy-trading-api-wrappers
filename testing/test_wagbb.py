from energy_trading_api import wagbb as w
from energy_trading_api import jepx as j


def test_actualFlow():
    # load capacity outlook
    assert not w.actualFlow().empty

def test_actualFlowDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.actualFlow(gasDay).empty


def test_ForecastFlow():
    # load capacity outlook
    assert not w.forecastFlow().empty

def test_ForecastFlowDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.forecastFlow(gasDay).empty




# df = w.largeUserConsumptionByCategory()
# filter for DBNGP Pipeline
# print(df[df['zoneName']=='Pilbara'].to_string())

# print (j.spotLatest().to_string())