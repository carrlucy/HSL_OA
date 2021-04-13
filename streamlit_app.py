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
dcurl="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=dc"
df = pd.read_json(jsonurl)
#df2= pd.read_xml(dcurl)
st.write(df)
