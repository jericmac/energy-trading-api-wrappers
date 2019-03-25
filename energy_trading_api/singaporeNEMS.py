import pandas as pd
from datetime import timedelta
from datetime import datetime
import numpy as np

def __call_api(endpoint,date_str):
    url = f"https://www.emcsg.com/marketdata/{endpoint}"

    try:
        df = pd.read_html(url)
        numberTables = df.__len__()
        lastTable = numberTables - 1
        df1 = df[lastTable]
        #convert date row to datetime then set it to the correct index
        for i, row in df1.iterrows():
            minutes_add = ((df1.at[i, 'PERIOD'] * 30) - 30)
            df1.at[i, 'DATE'] = datetime.strptime(date_str, '%Y-%m-%d') + timedelta(
                minutes=minutes_add.astype(np.float64))
        df1.set_index('DATE', inplace=True)
        return df1
    except Exception as e:
        print(e)
        return None


def singaporeUSEP(date="2019-01-01"):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')
    date_str = datetime.strftime(datetime_obj, '%d+%b+%Y')

    endpoint = f"priceinformation?doAccessData=true&USEP_accessAction=dataView&USEP_date={date_str}&dataType=USEP"
    return __call_api(endpoint,date)

