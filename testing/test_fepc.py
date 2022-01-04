from energy_trading_api import japanFEPC as j

def test_generationFacilityByCompany():
    assert not j.generationFacilityByCompany().empty

def test_generationFacilityByServiceArea():
    assert not j.generationFacilityByServiceArea().empty

def test_purchaseContracts():
    assert not j.purchaseContracts().empty

def test_substationFacility():
    assert not j.substationFacility().empty

def test_transmissionFacility():
    assert not j.transmissionFacility().empty

def test_electricityGeneratedAndPurchased():
    assert not j.electricityGeneratedAndPurchased().empty

def test_demandWithOptionalSupplyProvisionsPre1999():
    assert not j.demandWithOptionalSupplyProvisionsPre1999().empty

def test_numberOfCustomersForLightingAndPowerDemands():
    assert not j.numberOfCustomersForLightingAndPowerDemands().empty

def test_contractedDemandsInLightingAndPowerSections():
    assert not j.contractedDemandsInLightingAndPowerSections().empty

def test_electricityConsumedInLightingAndPowerSections():
    assert not j.electricityConsumedInLightingAndPowerSections().empty

def test_electricityConsumedByIndustry():
    assert not j.electricityConsumedByIndustry().empty

def test_electricityLossRate():
    assert not j.electricityLossRate().empty

def test_fuelTrackRecord():
    assert not j.fuelTrackRecord().empty

def test_hydroelectricFlowRate():
    assert not j.hydroelectricFlowRate().empty

def test_maximumPeakLoad():
    assert not j.maximumPeakLoad().empty

def test_earningsSummary():
    assert not j.earningsSummary().empty

def test_balanceSheetAssets():
    assert not j.balanceSheetAssets().empty

def test_balanceSheetLiabilityAndEquity():
    assert not j.balanceSheetLiabilityAndEquity().empty

def test_profitAndLoss():
    assert not j.profitAndLoss().empty

def test_fundRaisingTrackRecord():
    assert not j.fundRaisingTrackRecord().empty

def test_demandByUse():
    assert not j.demandByUse().empty

def test_demandByIndustry():
    assert not j.demandByIndustry().empty