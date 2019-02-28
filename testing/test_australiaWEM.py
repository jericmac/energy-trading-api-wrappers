from energy_trading_api import australiaWEM as a


def test_participants():
    assert not a.participants().empty

def test_facilities():
    assert not a.facilities().empty

def test_commissioningTest():
    assert not a.commissioningTest("2018").empty

def test_loadForecast():
    assert not a.loadForecast().empty

def test_extendedLoadForecast():
    assert not a.extendedLoadForecast().empty

def test_historicalLoadForecast():
    assert not a.historicalLoadForecast("2018").empty

def test_nonbalancingDispatchMeritOrder():
    assert not a.nonbalancingDispatchMeritOrder("2019-01").empty

def test_demandSideProgrammePrices():
    assert not a.demandSideProgrammePrices("2019").empty

def test_operationalMeasurements():
    assert not a.operationalMeasurements("2019").empty

def test_facilitySCADA():
    assert not a.facilitySCADA("2019-01").empty

def test_loadSummary():
    assert not a.loadSummary("2018").empty

def test_outages():
    assert not a.outages("2019").empty

def test_ircrRatios():
    assert not a.ircrRatios().empty

def test_peakSWISIntervals():
    assert not a.peakSWISIntervals().empty

def test_realTimeOutages():
    assert not a.realTimeOutages().empty

def test_repoCount():
    assert not a.repoCount().empty

def test_dispatchAdvisory():
    assert not a.dispatchAdvisory().empty

def test_marketAdvisory():
    assert not a.marketAdvisory().empty

def test_balancingSummary():
    assert not a.balancingSummary("2019").empty

def test_effectiveBalancingSubmission():
    assert not a.effectiveBalancingSubmission("2019-01").empty

def test_stemSummary():
    assert not a.stemSummary("2019").empty


def test_stemParticipantActivity():
    assert not a.stemParticipantActivity("2019-01").empty


def test_stemBidsAndOffers():
    assert not a.stemBidsAndOffers("2019-01").empty

def test_stemFacilityDeclarations():
    assert not a.stemFacilityDeclarations("2019-01").empty




