import math
import pandas as pd
import streamlit as st
import numpy as np
import json
import xml.etree.ElementTree as ET
import urllib.request
"""
# Welcome to The HSL Library Open Data Dashboard
"""
#these lines were used to test the json response thata worked fine however did not return affiliation data
#jsonurl="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=virginia&format=json"
#df = pd.read_json(jsonurl)
#st.write(df)

#here's the current working model in dublin core 
dcurl = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=University%20of%20Virginia&format=dc'
response = urllib.request.urlopen(dcurl).read()
dcElement = ET.fromstring(response) #fromstring returns an element
#dcElementTree = ET.parse(response) #parse returns an element tree
#newroot = dcElementTree.getroot()

#for contributor in dcElement.findall('dc:contributor'):
#  rank = country.find('rank').text
#  name = country.get('name')
st.write(dcElement.tag)

