"""
Australian NG Market General APIs

List of APIs:
    - Gas Scheme Register
"""


import pandas as pd

def __call_api_AEMC():
    url = "https://www.aemc.gov.au/energy-system/gas/gas-scheme-register"
    df = pd.read_html(url, index_col="Title")
    df[0].columns = ['State', 'Type', 'Operator', 'Comments']
    return df[0]

def pipelineRegister():
    return __call_api_AEMC()

def pipelineRegisterSearch(state="",operator="",type=""):
    df = __call_api_AEMC()

    if state!="":
        df = df.loc[df["State"].str.contains(state)]

    if operator!="":
        df = df.loc[df["Operator"].str.contains(operator)]

    if type!="":
        df = df.loc[df["Type"].str.contains(type)]

    return df


