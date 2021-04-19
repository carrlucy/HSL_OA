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
#these lines were used to test the json response thata worked fine however did not return affiliation data
#jsonurl="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=virginia&format=json"
#df = pd.read_json(jsonurl)
#st.write(df)

#here's the current working model in dublin core 
dcurl = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=University%20of%20Virginia&format=xml'
response = urllib.request.urlopen(dcurl).read()
dcElement = ET.fromstring(response) #fromstring returns an element
#dcElementTree = ET.parse(response) #parse returns an element tree
#newroot = dcElementTree.getroot()

#https://www.foxinfotech.in/2019/04/python-how-to-read-xml-from-url.html
var_url = urlopen('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=University%20of%20Virginia&format=xml')
xmldoc = parse(var_url)
xml_element=xmldoc.getroot('resultList')
st.write(xml_element)

#https://stackoverflow.com/questions/44392243/how-to-fetch-all-the-child-nodes-of-an-xml-using-python
#for child in root:
#  print({x.tag for x in root.findall(child.tag+"/*")})

#https://www.tutorialspoint.com/How-to-get-specific-nodes-in-xml-file-in-Python

#for node in xmldoc.findall("//isOpenAccess['=y']"):
#    for type in node.getchildren():
#        st.write(type.text)
#for item in xmldoc.iterfind('rdf'):
#  title = item.findtext('dc:title')
#  st.write(item)

#trying with rdflib here... 
#rdfData=rdflib.graph()
#n3=rdfData.parse(dcurl, format='application/rdf+xml')
#import zeep
#from zeep import Client, Settings
#settings = Settings(strict=False, xml_huge_tree=True)
#client = Client('https://www.ebi.ac.uk/europepmc/webservices/soap?wsdl', settings=settings)

#st.write(client.settings)
