import math
import streamlit as st
import numpy as np
import json
import rdflib
import altair as alt
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import urllib
import urllib.parse as urlparse
import requests
import pandas as pd
@st.cache()


dct = {}
for col in ['oa','author','date','title','iso','doi']:
    dct[col] = []

cr_mrk= '' #current cursor mark
nxt_mrk = '*' #next cursor mark

while cr_mrk != nxt_mrk:              
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?'
    query = '(AFF:"University of Virginia") AND (FIRST_PDATE:[2020-01-01 TO 2020-12-31]) AND (HAS_FT:Y)'
    params = {'query':query, 'resultType':'core', 'synonym':'TRUE','cursorMark':nxt_mrk,'pageSize':'1000','format':'json'}
    response = requests.get(url,params)
    rjson = response.json()
    #print(rjson)
    cr_mrk = urlparse.unquote(rjson['request']['cursorMark'])
    nxt_mrk = urlparse.unquote(rjson['nextCursorMark'])
    for rslt in rjson['resultList']['result']:
        dct['oa'].append(rslt['isOpenAccess']) if 'oa' in rslt.keys() else dct['oa'].append(0)
        dct['author'].append(rslt['authorString']) if 'authorString' in rslt.keys() else 0
        dct['date'].append(rslt['firstPublicationDate']) if 'firstPublicationDate' in rslt.keys() else dct['author'].append(0)
        dct['title'].append(rslt['title']) if 'title' in rslt.keys() else dct['title'].append(0)
        dct['iso'].append(rslt['isoabbreviation']) if 'isoabbreviation' in rslt.keys() else dct['iso'].append(0)
        dct['doi'].append(rslt['doi']) if 'doi' in rslt.keys() else dct['doi'].append(0)
        #print(dct)

#df=pd.DataFrame.from_dict(rslt)        
st.write(dct)
        
#df = pd.DataFrame({'Authors':authors,'ArticleTitle':title,'JournalTitle':iso,'date':date,'DOI':doi,'openAccess': openAccess})
#df['date'] = pd.to_datetime(df['date'])


#openFilter = sorted(df['openAccess'].drop_duplicates()) # select the open access values 
#open_Filter = st.sidebar.selectbox('Open Access?', openFilter) # render the streamlit widget on the sidebar of the page using the list we created above for the menu
#df2=df[df['openAccess'].str.contains(open_Filter)] # create a dataframe filtered below
#st.write(df2.sort_values(by='date'))


#df['year']=df['date'].dt.to_period('Y')
#df['yearDate'] = df['year'].astype(str)
#df3 = df[['yearDate','oa']].copy()

#dfChart=df3.groupby(['yearDate','openAccess'])['uid'].count()


#st.write(dfChart)
#st.write(dfChart.describe())




#valChart = alt.Chart((dfChart).mark_bar(opacity=1).encode(x='yearDate', y='uid'))

##b = alt.Chart(df4).mark_area(opacity=0.6).encode(x='name', y='salary')

#valLayer = alt.Chart(df3).mark_bar().encode(x='yearDate',y='count(openAccess)',color='openAccess')#

#st.altair_chart(valLayer, use_container_width=True)
