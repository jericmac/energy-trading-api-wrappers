from energy_trading_api import wagbb as w
from energy_trading_api import jepx as j

# load capacity outlook
df = w.capacityOutlook(gasDay="2018-01-01")
df = w.largeUserConsumptionByCategory()
# filter for DBNGP Pipeline
# print(df[df['zoneName']=='Pilbara'].to_string())

print (j.spotLatest().to_string())