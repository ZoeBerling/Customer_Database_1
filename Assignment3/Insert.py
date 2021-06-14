
"""Import Data from CSV (and eventually API) into database tables by importing in the DAO classes"""
from Cx_InsertsDOA import CxInsertsDAO

import pandas as pd

# print(data)
DOA = CxInsertsDAO()

df = pd.read_csv("sampleinsert.csv")
df['Review'] = df['Review'].str.replace("'", "`")
df['Experience'] = df['Experience'].str.replace("'", "`")

for i in range(len(df)):
    DOA.insertfreeprod(df['Time Stamp'][i], df['Product to Ship'][i], df['Email Address'][i])
    DOA.insertcustomer(df['Time Stamp'][i],df['Email Address'][i], df['Phone Number'][i], df['First'][i], df['Last Name'][i])
    DOA.insertaddress(df['Email Address'][i], df['Address'][i], df['City'][i], df['State'][i], df['Zip Code'][i])
    DOA.insertorder(df['Time Stamp'][i], df['Amazon Order Id'][i], df['Suppliment buy'][i], df['Choose Days'][i], df['Experience'][i], df['Review'][i])
