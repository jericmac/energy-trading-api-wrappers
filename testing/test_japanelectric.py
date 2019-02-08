from energy_trading_api import japanElectricity as j


def test_kyushuElectricJapanese():
    assert not j.kyushuElectricdemandJapanese("20190101").empty

def test_kyushuElectricEnglish():
    assert not j.kyushuElectricdemandEnglish("20190101").empty

def test_kyushuElectric5MSJapanese():
    assert not j.kyushuElectricDemand5MSJapanese("20190101").empty

def test_kyushuElectric5MSEnglish():
    assert not j.kyushuElectricDemand5MSEnglish("20190101").empty