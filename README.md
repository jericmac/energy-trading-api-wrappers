# Energy Trading API Wrappers
This package aims to build Pandas-based API wrappers for Energy Markets Data coming from publicly available sources.
The results are returned in the Pandas dataFrame format unless specified otherwise.

> **disclaimer** While readily useable, this API library is under constant in development. The reliability of the data from  the API list depends on the sources.
 Enjoy!

Supported APIs:
> **Australia**
- [Western Australia Gas Bulletin Board](https://gbbwa.aemo.com.au/)
- [ACCC LNG Netback Price Index](https://www.accc.gov.au/regulated-infrastructure/energy/gas-inquiry-2017-2020/lng-netback-price-series)
- [Australian REC Register](https://www.rec-registry.gov.au/)
- [AEMC Gas Scheme Register (developing)](https://www.aemc.gov.au/energy-system/gas/gas-scheme-register)
- [Western Australia Wholesale Electricity Market (WEM)](http://data.wa.aemo.com.au/#)
- [Bureau of Meteorology](http://www.bom.gov.au/)

> **Singapore**
- [Singapore National Electricity Market (NEMS)](https://www.emcsg.com/)


> **Japan**
- [Japan Electric Power Exchange](http://www.jepx.org/)
- [Kyushu Electric Power Company - H/5M Demand and Forecasted Demand](http://www.kyuden.co.jp)
- [Chubu Electric Power Company - Hourly Historical and Current Demand](http://denki-yoho.chuden.jp)
- [Tokyo Electric Power Company - Hourly Historical and Current Demand](http://tepco.co.jp)
- [Chugoku Electric Power Company - Hourly Historical Demand](https://www.energia.co.jp/)
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
##### Western Australian Wholesale Electricity Market (WEM)
```python
from energy_trading_api import australiaWEM 
df = australiaWEM.loadForecast()
df1 = australiaWEM.demandSideProgrammePrices(year="2019")

```   
[WEM Data API Documentation](http://data.wa.aemo.com.au/#)

##### ACCC LNG Netback Price Series
```python
from energy_trading_api import australiaLNG
netback,netforward,merged = australiaLNG.acccNetbackPrice()
print(netback.head())
```   

[ACCC LNG Netback Price Series Documentation](https://www.accc.gov.au/system/files/Guide%20to%20the%20LNG%20netback%20price%20series%20-%20October%202018.pdf)


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

##### Australian Bureau of Meteorology
Retrieves BOM records into a pandas dataframe, given Product and location.

For instance, Bankstown time series data has a product code of IDN60901.94765.

To return Air Temp, Apparent Temp Rel Humidity, Cloud data in a pandas df, simply do:

```python
from energy_trading_api import australiaBOM 
df1 = australiaBOM.airTemp('IDN60901.94765')
df2 = australiaBOM.apparentTemp('IDN60901.94765')
df2 = australiaBOM.relativeHumidity('IDN60901.94765')
df3 = australiaBOM.cloud('IDN60901.94765')

```    

You can also access the entire dataset by doing:

```python
from energy_trading_api import australiaBOM 
df, df_header = australiaBOM.__call_api_BOM('IDN60901.94765')
# e.g. dew point:
print(df['dewpt'].to_string())
```    


[Bankstown BOM Data Example](http://www.bom.gov.au/products/IDN60901/IDN60901.94765.shtml)



 ### SINGAPORE
##### Singapore National Electricity Market (NEMS)

```python
from energy_trading_api import singaporeNEMS 
df = singaporeNEMS.singaporeUSEP(date="2019-01-01")
```    

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

 ##### CHUGOKU Electric Power Company (Chugoku Denki)
```python
from energy_trading_api import japanElectricity as je 
df = je.chugokuElectricDemandJapanese("2018")

```  


### GLOBAL
##### U.S. Energy Information Administration
```python
from energy_trading_api import eia_api 
df = eia_api.ngAustraliaProduction("<YOUR-API-KEY-HERE>")
```    
[EIA-Python Documentation](https://github.com/mra1385/EIA-python)
[EIA API Documentation](https://www.eia.gov/opendata/commands.php)