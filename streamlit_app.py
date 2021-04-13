import math
import pandas as pd
import streamlit as st
import numpy as np
import json
"""
# Welcome to The HSL Library Open Data Dashboard
"""

df = pd.read_json('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=json')
df = pd.DataFrame(df['result'].values.tolist())
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df = df.set_index('TimeStamp')
print (df.head())
