from energy_trading_api import wagbb as w
from energy_trading_api import jepx as j


def test_actualFlow():
    # load capacity outlook
    assert not w.actualFlow().empty

def test_actualFlowDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.actualFlow(gasDay).empty

def test_endUserConsumption():
    # load capacity outlook
    assert not w.endUserConsumption().empty

def test_endUserConsumptionDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.endUserConsumption(gasDay).empty

def test_largeUserConsumptionByCategory():
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory().empty

def test_largeUserConsumptionByCategoryDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory(gasDay).empty

def test_mediumTermCapacity():
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory().empty

def test_mediumTermCapacityDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory(gasDay).empty

def test_gasSpecification():
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory().empty

def test_gasSpecificationDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory(gasDay).empty

def test_largeUserConsumption():
    # load capacity outlook
    assert not w.largeUserConsumption().empty

def test_largeUserConsumptionDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumption(gasDay).empty

def test_capacityOutlook():
    # load capacity outlook
    assert not w.capacityOutlook().empty

def test_capacityOutlookDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.capacityOutlook(gasDay).empty

def test_linepackCapacityAdequacy():
    # load capacity outlook
    assert not w.linepackCapacityAdequacy().empty

def test_linepackCapacityAdequacyDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.linepackCapacityAdequacy(gasDay).empty


def test_ForecastFlow():
    # load capacity outlook
    assert not w.forecastFlow().empty

def test_ForecastFlowDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.forecastFlow(gasDay).empty