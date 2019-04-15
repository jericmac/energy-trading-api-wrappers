from energy_trading_api import australiaLNG


def test_acccNetbackPrice():
    a,b,c = australiaLNG.acccNetbackPrice()
    assert not a.empty & b.empty & c.empty