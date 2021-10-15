from collections import namedtuple
import math
import pandas as pd
import streamlit as st




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
df3[['transaction_sale','features_suite','features_bedroom','total_area','features_garage','features_bathroom','sqrmeter_price_area_sale','harvesine_distance', 'original_address_neighborhood','state_name','city_raw']]

       