from datetime import timedelta
from datetime import datetime


class commonData:
    dictEiaReports = dict ([
        #region COAL
            #region Production
        ('worldCoalProduction','INTL.4411-1-WORL-QBTU.A'),
        ('africaCoalProduction','INTL.4411-1-AFRC-QBTU.A'),
        ('australiaCoalProduction','INTL.4411-1-AUS-QBTU.A'),
        ('chinaCoalProduction', 'INTL.4411-1-CHN-QBTU.A'),
        ('asiaCoalProduction','INTL.4411-1-ASOC-QBTU.A'),
        ('northAmericaCoalProduction','INTL.4411-1-NOAM-QBTU.A'),
        ('europeCoalProduction', 'INTL.4411-1-EURO-QBTU.A'),

            #endregion Production
            # region Consumption
         ('worldCoalConsumption', 'INTL.4411-2-WORL-QBTU.A'),
         ('africaCoalConsumption', 'INTL.4411-2-AFRC-QBTU.A'),
         ('australiaCoalConsumption', 'INTL.4411-2-AUS-QBTU.A'),
         ('chinaCoalConsumption', 'INTL.4411-2-CHN-QBTU.A'),
         ('asiaCoalConsumption', 'INTL.4411-2-ASOC-QBTU.A'),
         ('northAmericaCoalConsumption', 'INTL.4411-2-NOAM-QBTU.A'),
         ('europeCoalConsumption', 'INTL.4411-2-EURO-QBTU.A'),
         ('southAmericaCoalConsumption', 'INTL.4411-2-CSAM-QBTU.A'),
            # endregion Consumption
        #endregion COAL

        # region NG
        # region Production
        ('worldNGProduction', 'INTL.4413-1-WORL-QBTU.A'),
        ('africaNGProduction', 'INTL.4413-1-AFRC-QBTU.A'),
        ('australiaNGProduction', 'INTL.4413-1-AUS-QBTU.A'),
        ('chinaNGProduction', 'INTL.4413-1-CHN-QBTU.A'),
        ('asiaNGProduction', 'INTL.4413-1-ASOC-QBTU.A'),
        ('northAmericaNGProduction', 'INTL.4413-1-NOAM-QBTU.A'),
        ('europeNGProduction', 'INTL.4413-1-EURO-QBTU.A'),

        # endregion Production
        # region Consumption
        ('worldNGConsumption', 'INTL.4413-2-WORL-QBTU.A'),
        ('africaNGConsumption', 'INTL.4413-2-AFRC-QBTU.A'),
        ('australiaNGConsumption', 'INTL.4413-2-AUS-QBTU.A'),
        ('chinaNGConsumption', 'INTL.4413-2-CHN-QBTU.A'),
        ('asiaNGConsumption', 'INTL.4413-2-ASOC-QBTU.A'),
        ('northAmericaNGConsumption', 'INTL.4413-2-NOAM-QBTU.A'),
        ('europeNGConsumption', 'INTL.4413-2-EURO-QBTU.A'),
        ('southAmericaNGConsumption', 'INTL.4413-2-CSAM-QBTU.A'),
        # endregion Consumption

        # region Price
        ('henryHubNGSpotPriceDaily', 'NG.RNGWHHD.D'),
        # endregion Price
        # endregion NG

        # region CRUDE
        # region Price
        ('wtiCushingSpotPriceDaily', 'PET.RWTC.D'),
        # endregion Price
        # endregion CRUDE

    ])


def combineTimePeriodDate(dF,targetColumn='DATETIME',periodColumn='PERIOD',targetColumnFmt ='%Y/%m/%d' ):
    for i, row in dF.iterrows():
        minutes_add = ((int(dF.at[i, periodColumn]) * 30) - 30)
        dF.at[i, targetColumn] = datetime.strptime(dF.at[i, targetColumn], targetColumnFmt) + timedelta(minutes=int(minutes_add))
    dF.set_index(targetColumn, inplace=True)
    return dF


mappingJEPX = ({0:'DATETIME'
,1:'PERIOD'
,2:'Selling bid amount (kWh)'
,3:'buying bid amount (kWh)'
,4:'execution total amount (kWh)'
,5:'system price (JPY/kWh)'
,6:'Area price Hokkaido (JPY/kWh)'
,7:'Area price Tohoku (JPY/kWh)'
,8:'Area price Tokyo (JPY/kWh)'
,9:'Area Price Chubu (JPY/kWh)'
,10:'Area Price Hokuriku (JPY/kWh)'
,11:'Area Price Kansai (JPY/kWh)'
,12:'Area Price Chuugoku (JPY/kWh)'
,13:'Area Price Shikoku (JPY/kWh)'
,14:'Area price Kyushu (JPY/kWh)'
,15:'spot · time before average price (JPY/kWh)'
,16:'upper limit value × spot time before average price (JPY/kWh) '
,17:'lower limit value × spot · time before average price (JPY/kWh)'
,18:'preliminary value × spot · time before average price (JPY/kWh)'
,19:'confirmed value × spot · time before average price (JPY/kWh)'
,20:'avoidable cost national price (JPY/kWh)'
,21:'avoidable Cost Hokkaido (JPY/kWh)'
,22:'avoidable cost Tohoku (JPY/kWh)'
,23:'avoidable cost Tokyo (JPY/kWh)'
,24:'avoidable cost Chubu (JPY/kWh)'
,25:'avoidable cost Hokuriku (JPY/kWh)'
,26:'avoidable Cost Kansai (JPY/kWh)'
,27:'avoidable Cost Chuugoku (JPY/kWh)'
,28:'avoid Noh cost Shikoku (JPY/kWh)'
,29:'avoidable cost Kyushu (JPY/kWh)'
                        })