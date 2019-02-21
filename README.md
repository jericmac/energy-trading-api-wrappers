# Energy Trading API Wrappers
This package aims to build Pandas-based API wrappers for Energy Markets Data coming from publicly available sources.
The results are returned in the Pandas dataFrame format unless specified otherwise.

> **disclaimer** While readily useable, this API library is under constant in development. The reliability of the data from  the API list depends on the sources.
 Enjoy!

Supported APIs:
> **Australia**
- [Western Australia Gas Bulletin Board](https://gbbwa.aemo.com.au/)
- [Australian REC Register](https://www.rec-registry.gov.au/)
- [AEMC Gas Scheme Register (developing)](https://www.aemc.gov.au/energy-system/gas/gas-scheme-register)

> **Japan**
- [Japan Electric Power Exchange](http://www.jepx.org/)
- [Kyushu Electric Power Company - H/5M Demand and Forecasted Demand](http://www.kyuden.co.jp)
- [Chubu Electric Power Company - Hourly Historical and Current Demand](http://denki-yoho.chuden.jp)
- [Tokyo Electric Power Company - Hourly Historical and Current Demand](http://tepco.co.jp)
> **Global**
- [U.S. Energy Information Administration Open Data](https://www.eia.gov/opendata/)

## Installation
* Python 3.6 or 3.7

To install,  use `pip` :
```bash
$ pip install energy-trading-api
```

### Requirements
* Python 3.7


## Usage
### AUSTRALIA
##### Australian REC Register
```python
from energy_trading_api import australiaREC 
df = australiaREC.recDay("2019-01-01")


```   
[REC Registry API Documentation](http://www.cleanenergyregulator.gov.au/DocumentAssets/Pages/REC-Registry-API-specifications.aspx)


##### AEMC Gas Scheme Register
```python
from energy_trading_api import australiaNG 
df = australiaNG.pipelineRegister()
df1 = australiaNG.pipelineRegisterSearch(state="NSW",operator="APA Group")

```   
[AEMC Gas Scheme Register Website](https://www.aemc.gov.au/energy-system/gas/gas-scheme-register)

##### Western Australia Gas Bulletin Board
```python
from energy_trading_api import wagbb 
wagbb.capacityOutlook()
```    
[WAGBB API Documentation](https://gbbwa.aemo.com.au/api/v1/document/1f2bc41e-3e42-41eb-86f7-4a10d2d6e4bc/content)

 

### JAPAN
##### Japan Electric Power Exchange
```python
from energy_trading_api import jepx 
df = jepx.spotLatest()
df = jepx.spotLatest("20190101")
```  

##### Kyushu Electric Power Company (Kyuden)
```python
from energy_trading_api import japanElectricity as je 
df = je.kyushuElectricdemandJapanese()
df1 = je.kyushuElectricdemandJapanese(day="20190101")
```  
 ##### Chubu Electric Power Company (Chuden)
```python
from energy_trading_api import japanElectricity as je 
df = je.chubuElectricdemandJapanese()
df1 = je.chubuElectricDemandJapaneseRange(begtime="20190101",endtime="20190101")
```  

 ##### Tokyo Electric Power Company (TEPCO)
```python
from energy_trading_api import japanElectricity as je 
df = je.tepcoElectricDemandHistoricalJapanese("2018")
df1 = je.tepcoElectricDemandCurrentJapanese()
```  


### GLOBAL
##### U.S. Energy Information Administration
```python
from energy_trading_api import eia_api 
df = eia_api.ngAustraliaProduction("<YOUR-API-KEY-HERE>")
```    
[EIA-Python Documentation](https://github.com/mra1385/EIA-python)
[EIA API Documentation](https://www.eia.gov/opendata/commands.php)