from energy_trading_api import australiaREC as a


def test_pipelineRegister():
    assert not a.recDay("2019-01-01").empty