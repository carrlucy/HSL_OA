import math
import streamlit as st
import numpy as np
import json
import rdflib
import altair as alt
from urllib.request import urlopen
#from xml.etree.ElementTree import parse
import urllib
import urllib.parse as urlparse
import requests
import pandas as pd
#@st.cache




#fulltext_list


@st.cache(suppress_st_warning=True)
def bigask ():
    dct = {}
    for col in ['oa','author','year','title','doi','id','cited']:
        dct[col] = []

    cr_mrk= '' #current cursor mark
    nxt_mrk = '*' #next cursor mark
    while cr_mrk != nxt_mrk:              
        url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?'
        query = '(AFF:"University of Virginia") AND (FIRST_PDATE:[2014-12-31 TO 2020-12-31])'
        params = {'query':query, 'resultType':'core', 'synonym':'TRUE','cursorMark':nxt_mrk,'pageSize':'1000','format':'json'}
        response = requests.get(url,params)
        rjson = response.json()
        cr_mrk = urlparse.unquote(rjson['request']['cursorMark'])
        nxt_mrk = urlparse.unquote(rjson['nextCursorMark'])
        for rslt in rjson['resultList']['result']:
            dct['author'].append(rslt['authorString']) if 'authorString' in rslt.keys() else dct['author'].append(0)
            dct['year'].append(rslt['pubYear']) if 'pubYear' in rslt.keys() else dct['year'].append(0)
            dct['title'].append(rslt['title']) if 'title' in rslt.keys() else dct['title'].append(0)
            dct['doi'].append(rslt['doi']) if 'doi' in rslt.keys() else dct['doi'].append(0)
            dct['id'].append(rslt['id']) if 'id' in rslt.keys() else dct['id'].append(0)
            dct['oa'].append(rslt['isOpenAccess']) if 'isOpenAccess' in rslt.keys() else dct['oa'].append(0)
            dct['cited'].append(rslt['citedByCount']) if 'citedByCount' in rslt.keys() else dct['cited'].append(0)  
            #dct['journal'].append(rslt['journalInfo']['journal']['title']) if ['journalInfo']['journal']['title'] in rslt.keys() else dct['journal'].append(0)  
    df=pd.DataFrame.from_dict(dct, orient='columns')
        #print(dct)
    return df


#menu = ["Y", "N"]
#st.sidebar.subheader("Select Option")
#choice = st.sidebar.selectbox("Full Text", menu)

dfdata=bigask()
#dfdata= dfdata[dfdata['oa'] == choice] 
#df=pd.DataFrame.from_dict(rslt)        

citations = st.sidebar.slider('Number of citations', 0, 100, 1)
dfdata = dfdata[dfdata['cited'] >= citations] 

#dfdata
st.write(dfdata)
        


#openFilter = sorted(df['openAccess'].drop_duplicates()) # select the open access values 
#open_Filter = st.sidebar.selectbox('Open Access?', openFilter) # render the streamlit widget on the sidebar of the page using the list we created above for the menu
#df2=df[df['openAccess'].str.contains(open_Filter)] # create a dataframe filtered below
#st.write(df2.sort_values(by='date'))




valLayer = alt.Chart(dfdata).mark_bar().encode(x='year',y='count(oa)',color='oa')#

st.altair_chart(valLayer, use_container_width=True)
