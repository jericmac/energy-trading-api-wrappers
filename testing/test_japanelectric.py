from energy_trading_api import japanElectricity as j

#region test kyuden
def test_kyushuElectricJapanese():
    assert not j.kyushuElectricDemandJapanese("20190101").empty

def test_kyushuElectricEnglish():
    assert not j.kyushuElectricDemandEnglish("20190101").empty

def test_kyushuElectric5MSJapanese():
    assert not j.kyushuElectricDemand5MSJapanese("20190101").empty

def test_kyushuElectric5MSEnglish():
    assert not j.kyushuElectricDemand5MSEnglish("20190101").empty

#endregion test kyuden

#region test chuden
def test_chubuElectricdemandJapanese():
    assert not j.chubuElectricDemandJapanese().empty

def test_chubuElectricdemandEnglish():
    assert not j.chubuElectricDemandEnglish().empty

def test_chubuElectricDemandJapaneseRange():
    assert not j.chubuElectricDemandJapaneseRange(begtime = "20180101",endtime="20180201").empty

def test_chubuElectricDemandEnglishRange():
    assert not j.chubuElectricDemandJapaneseRange(begtime = "20180101",endtime="20180201").empty
#endregion test chuden

#region test TEPCO
def test_tepcoElectricDemandCurrentJapanese():
    assert not j.tepcoElectricDemandCurrentJapanese().empty

def test_tepcoElectricDemandCurrentEnglish():
    assert not j.tepcoElectricDemandCurrentEnglish().empty

def test_tepcoElectricDemandHistoricalJapanese():
    assert not j.tepcoElectricDemandHistoricalJapanese("2018").empty

def test_tepcoElectricDemandHistoricalEnglish():
    assert not j.tepcoElectricDemandHistoricalEnglish("2018").empty
#endregion test TEPCO