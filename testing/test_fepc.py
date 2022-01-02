from energy_trading_api import japanElectricity as j

def test_generationFacilityByCompany():
    assert not j.generationFacilityByCompany().empty