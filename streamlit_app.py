import math
import pandas as pd
import streamlit as st
import numpy as np
import json
"""
# Welcome to The HSL Library Open Data Dashboard
"""
url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=virginia&format=json"
df = pd.read_json(url,orient='columns')

st.write(df['result'])
