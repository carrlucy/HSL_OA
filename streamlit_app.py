import math
import pandas as pd
import streamlit as st
import numpy as np
import json
"""
# Welcome to The HSL Library Open Data Dashboard
"""
url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=json"
df = pd.read_json(url)
#df = pd.DataFrame(df['result'].values.tolist())
print (df.head())
print (url)
"""
# Why no data
"""
