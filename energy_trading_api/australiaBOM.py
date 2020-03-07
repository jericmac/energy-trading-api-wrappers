import pandas as pd
import urllib.request
import json as json
from dateutil import parser as parser

__URL = "http://www.bom.gov.au/fwo"
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def __call_api_BOM(code):
    product, station = code.split('.')
    url = '%s/%s/%s.json' % (__URL, product, code)
    opener = AppURLopener()
    file = opener.open(url)
    stationJSON = json.loads(file.read())
    data = stationJSON['observations']['data']
    header_data = stationJSON['observations']['header']
    df = pd.DataFrame(data)
    df_header =pd.DataFrame(header_data)
    df['local_date_time_full'] = df['local_date_time_full'].apply(parser.parse)
    df.set_index('local_date_time_full', inplace=True)
    return df,df_header

def nameState(code):
    df, df_header = __call_api_BOM(code)
    name = df_header['name']
    state = df_header['state']
    return name+','+state

def airTemp(code):
    df,df_header = __call_api_BOM(code)
    return df['air_temp']

def apparentTemp(code):
    df,df_header = __call_api_BOM(code)
    return df['apparent_t']

def cloud(code):
    df,df_header = __call_api_BOM(code)
    return df['cloud']

def relativeHumidity(code):
    df,df_header = __call_api_BOM(code)
    return df['rel_hum']

