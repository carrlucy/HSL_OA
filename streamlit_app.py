import math
import pandas as pd
import streamlit as st
import numpy as np
import json
import xml.etree.ElementTree as ET
import urllib.request
from urllib.request import urlopen
from xml.etree.ElementTree import parse



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

#https://www.foxinfotech.in/2019/04/python-how-to-read-xml-from-url.html
var_url = urlopen('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=University%20of%20Virginia&format=dc')
xmldoc = parse(var_url)
#newroot=xmldoc._setroot('rdf')
st.write(xmldoc.iterfind('dc:contributor'))
#for item in xmldoc.iterfind('rdf'):
#  title = item.findtext('dc:title')
#  st.write(item)



