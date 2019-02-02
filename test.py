from energy_trading_api import wagbb as w

# load capacity outlook
df = w.capacityOutlook(gasDay="2018-01-01")
# filter for DBNGP Pipeline
print(df[df['facilityCode']=='DBNGP'].to_string())