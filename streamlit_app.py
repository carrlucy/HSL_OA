import math
import pandas as pd
import streamlit as st
import numpy as np
import json
import xml.etree.ElementTree as ET
import urllib.request
import rdflib
from urllib.request import urlopen
from xml.etree.ElementTree import parse



"""
# Welcome to The HSL Library Open Data Dashboard
"""
searchThis=st.sidebar.text_input('Query')

buildQuery=('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=' + searchThis + '&resultType=core&cursorMark=*&pageSize=35&format=xml')
#https://www.foxinfotech.in/2019/04/python-how-to-read-xml-from-url.html
restQuery=urlopen(buildQuery)
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
        st.write(b.tag, "contains", b.text)
    for c in root1.iter('authorString'):
        st.write(c.tag, "contains", c.text)
    for d in root1.iter('firstPublicationDate'):
        st.write(d.tag, "contains", d.text)
    for e in root1.iter('title'):
        st.write(e.tag, "contains", e.text)
    for f in root1.iter('ISOAbbreviation'):
        st.write(f.tag, "contains", f.text)  
    for g in root1.iter('doi'):
        st.write(g.tag, "contains", g.text)
    openAccess.append(b.text)
    authors.append(c.text)
    date.append(d.text)
    title.append(e.text)
    iso.append(f.text)
    doi.append(g.text)
    
df = pd.DataFrame({'openAccess': openAccess,'authors':authors,'date':date,'title':title,'iso':iso,'doi':doi})
st.write(df)
