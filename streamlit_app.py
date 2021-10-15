from collections import namedtuple
import math
import pandas as pd
import streamlit as st



def get_table_download_link2(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href


df = pd.read_csv("base_nit2.csv")
features = ['transaction_sale','features_suite','features_bedroom','total_area','features_garage','features_bathroom','sqrmeter_price_area_sale','harvesine_distance']

sel_amostra = st.selectbox(
    'Amostra',
     df.index.values)

'Selecionado: ', sel_amostra, df[features].iloc[sel_amostra]

#df

df2 = df[features]
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(df2.values)
X = scaler.transform(df2.values)

from sklearn.metrics import pairwise_distances
dist = pairwise_distances(X, metric='euclidean')

ordenada = list(enumerate(list( dist[sel_amostra] )))
ordenada.sort(key=lambda tup: tup[1]) 


selec = []
for i in ordenada[0:10]:
  #print(pd.DataFrame(df.iloc[i[0]]))
  selec.append(i[0])

  
df3 = df.iloc[selec]
"""
 # Semelhantes (top 10)

 O primeiro da lista é a amostra selecionada
"""
df4 = df3[['transaction_sale','features_suite','features_bedroom','total_area','features_garage','features_bathroom','sqrmeter_price_area_sale','harvesine_distance', 'original_address_neighborhood','state_name','city_raw']]
df4

from io import BytesIO
import base64
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download xls </a>' 

st.markdown(get_table_download_link(df4), unsafe_allow_html=True)

