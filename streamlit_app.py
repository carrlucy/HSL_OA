import math
import pandas as pd
import streamlit as st
import numpy as np
import json
import xml.etree.ElementTree as ET
import urllib.request
import rdflib
import altair as alt
from urllib.request import urlopen
from xml.etree.ElementTree import parse



"""
# EuropePMC Open Data Dashboard
"""
#searchThis=st.sidebar.text_input('Query EuropePMC', 'Virginia')

#buildQuery=('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=' + searchThis + '&resultType=core&cursorMark=*&pageSize=35&format=xml')
builtQuery=('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=University%20of%20Virginia&resultType=core&cursorMark=*&pageSize=200&format=xml')

#https://www.foxinfotech.in/2019/04/python-how-to-read-xml-from-url.html
restQuery=urlopen(builtQuery)
#st.write(restQuery)
xmlTree=ET.parse(restQuery)
root = xmlTree.getroot()


#st.write(root[4][0][0].text)    
#https://towardsdatascience.com/converting-multi-layered-xml-files-to-dataframes-in-python-using-xmltree-a13f9b043b48
#for a in root[4]:
#    st.write(a.text)

openAccess=[]
authors=[]
date=[]
title=[]
iso=[]
doi=[]


for a in root[4]:
    root1=ET.Element('result')
    root1=a
    for b in root1.iter('isOpenAccess'):
        root2=ET.Element('root')
        #st.write(b.tag, "contains", b.text)
    for c in root1.iter('authorString'):
        root3=ET.Element('root2')
        #st.write(c.tag, "contains", c.text)
    for d in root1.iter('firstPublicationDate'):
        root4=ET.Element('root3')
        #st.write(d.tag, "contains", d.text)
    for e in root1.iter('title'):
        root5=ET.Element('root4')
        #st.write(e.tag, "contains", e.text)
    for f in root1.iter('ISOAbbreviation'):
        root6=ET.Element('root5')
        #st.write(f.tag, "contains", f.text)  
    for g in root1.iter('doi'):
        root7=ET.Element('root6')
        #st.write(g.tag, "contains", g.text)
    openAccess.append(b.text)
    authors.append(c.text)
    date.append(d.text)
    title.append(e.text)
    iso.append(f.text)
    doi.append(g.text)

    

df = pd.DataFrame({'openAccess': openAccess,'authors':authors,'date':date,'title':title,'iso':iso,'doi':doi})


openFilter = sorted(df['openAccess'].drop_duplicates()) # select the open access values 
open_Filter = st.sidebar.selectbox('Open Access?', openFilter) # render the streamlit widget on the sidebar of the page using the list we created above for the menu
df2=df[df['openAccess'].str.contains(open_Filter)] # create a dataframe filtered below
st.write(df2.sort_values(by='date'))
st.write(df2.describe())


dfChart = df2[['openAccess', 'date']].copy()
dfChart['Year'] = dfChart['date'].apply(lambda x: "%d" % (x.year))

st.write(dfChart)

#a = alt.Chart(dfChart).mark_area(opacity=1).encode(x='Year', y='openAccess')

#b = alt.Chart(df4).mark_area(opacity=0.6).encode(x='name', y='salary')

#c = alt.layer(a)

#st.altair_chart(c, use_container_width=True)
