from energy_trading_api import australiaBOM as a

__Bankstown = 'IDN60901.94765'

def test_genericBOM():
    assert not a.__call_api_BOM(__Bankstown).empty

def test_airTemp():
    assert not a.airTemp(__Bankstown).empty

def test_apparentTemp():
    assert not a.apparentTemp(__Bankstown).empty

def test_cloud():
    assert not a.cloud(__Bankstown).empty

def test_relativeHumidity():
    assert not a.relativeHumidity(__Bankstown).empty

def test_nameState():
    assert not a.nameState(__Bankstown).empty