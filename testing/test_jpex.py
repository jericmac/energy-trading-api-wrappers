from energy_trading_api import jepx as j

def test_spotLatest():
    # load capacity outlook
    assert not j.spotLatest().empty

def test_spotLatestDate(gasDay="20180101"):
    # load capacity outlook
    assert not j.spotLatest(gasDay).empty
