import pandas as pd
from lxml import html
import requests
import re

def determineLatestACCCreport(url_ACCC="https://www.accc.gov.au/regulated-infrastructure/energy/gas-inquiry-2017-2020/lng-netback-price-series"
                              ,urlPattern="https://www.accc.gov.au/system/files/LNG%20netback%20price%20series%20-%20Public*"):
    #Get ACCC website HTML
    r = requests.get(url_ACCC)
    webpage = html.fromstring(r.content)
    #Get a list of all HREF url's
    listx = webpage.xpath('//a/@href')

    #look for the Netback file pattern
    url_regex = re.compile(urlPattern)

    #search for the url using regex, then take the first record- this results in the latest ACCC Netback file url.
    newlist = list(filter(url_regex.match, listx))
    url = newlist[0]

    return url

def acccNetbackPrice(targetSheet="Price series chart data"
                     ,start_row=4
                     ,datecolumn=1
                     ,indexRename = "Delivery Month"
                     , netbackColumnRename = "Historical netback prices"
                     , netbackForwardColumnRename = "Forward netback prices"
                     ):
    #   take the latest ACCC netback price
    url = determineLatestACCCreport()

    #   read the excel file, and save it to a dataframe, note the targetsheet, and the datecolumn, which serves as the index
    df = pd.read_excel(url, index_col=datecolumn, sheet_name=targetSheet)

    #   filter the dataframe to start at a particular row, by default this is 4.
    df = df[start_row:]

    #   Rename Indexes
    df.index.rename(indexRename, inplace=True)

    #   Just Drop this index it's always zero, as it's the first row in the spreadsheet.
    df = df.drop("Unnamed: 0", axis=1)

    #   Rename the Netback Column
    df.rename(columns={"Unnamed: 2": netbackColumnRename}, inplace=True)

    #   Drop the NA records for the historical netbacks, save to the net back DF
    dfNetback = df[netbackColumnRename].dropna()

    # delete all the columns that have all-na records.
    df = df.dropna(axis=1, how='all')

    # get the last column - this is the latest forward netback, and save records to the net forward DF
    last_column = df.iloc[:, -1]
    dfNetforward = last_column.dropna()

    #merge the netback and netforward df's
    df_merged = pd.concat([dfNetback, dfNetforward], axis=1)
    df_merged.rename(columns={df_merged.columns[len(df_merged.columns) - 1]: netbackForwardColumnRename}, inplace=True)

    return dfNetback,dfNetforward,df_merged



