from energy_trading_api import singaporeNEMS as s

def test_singaporeUSEP():
    # load capacity outlook
    assert not s.singaporeUSEP(date="2019-01-01").empty