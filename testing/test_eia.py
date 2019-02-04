from energy_trading_api import eia_api

api_key ="<EIA API KEY GOES HERE>"


def test_australiaCoalProduction(key=api_key):
    # load capacity outlook
    assert not eia_api.coalAustraliaProduction(key=key).empty