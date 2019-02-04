from energy_trading_api import wagbb as w
from energy_trading_api import jepx as j


def test_actualFlow():
    # load capacity outlook
    assert not w.actualFlow().empty

def test_actualFlowDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.actualFlow(gasDay).empty


def test_ForecastFlow():
    # load capacity outlook
    assert not w.forecastFlow().empty

def test_ForecastFlowDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.forecastFlow(gasDay).empty

def test_endUserConsumption():
    # load capacity outlook
    assert not w.endUserConsumption().empty

def test_endUserConsumptionDate(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.endUserConsumption(gasDay).empty

def test_largeUserConsumptionByCategory():
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory().empty

def test_largeUserConsumptionByCategory(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory(gasDay).empty

def test_mediumTermCapacity():
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory().empty

def test_mediumTermCapacity(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory(gasDay).empty

def test_gasSpecification():
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory().empty

def test_gasSpecification(gasDay="2018-01-01"):
    # load capacity outlook
    assert not w.largeUserConsumptionByCategory(gasDay).empty
