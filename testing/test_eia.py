from energy_trading_api import eia_api

api_key ="<EIA API KEY GOES HERE>"

def test_australiaCoalProduction(key=api_key):
    assert not eia_api.coalAustraliaProduction(key=key).empty

def test_australiaCoalConsumption(key=api_key):
    assert not eia_api.coalAustraliaConsumption(key=key).empty

def test_eiaAPI(key=api_key,series_ID="PET.RBRTE.D"):
    assert not eia_api.eiaAPI(key=key,seriesID=series_ID).empty