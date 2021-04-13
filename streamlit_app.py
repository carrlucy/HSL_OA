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
jsonurl="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=virginia&format=json"

df = pd.read_json(jsonurl)
#st.write(df)


dcurl = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=dc'
response = urllib.request.urlopen(dcurl).read()
tree = ET.fromstring(response)
st.write(tree)
