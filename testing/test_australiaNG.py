from energy_trading_api import australiaNG as a


def test_pipelineRegister():
    assert not a.pipelineRegister().empty

def test_pipelineRegisterSearchState():
    assert not a.pipelineRegisterSearch(state="NSW").empty

def test_pipelineRegisterSearchType():
    assert not a.pipelineRegisterSearch(type="Distribution").empty

def test_pipelineRegisterSearchOperator():
    assert not a.pipelineRegisterSearch(operator="APA").empty