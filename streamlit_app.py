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
#xml_element=xmldoc.getroot()
#st.write(xml_element)



#for x in root.iter('region'):
#    root1=et.Element('root')
#    root1=x
#    for supply in root1.iter('AgSupplySector'):
#        root2=et.Element('root')
#        print(supply)
#        root2=(supply)
#        for tech in root2.iter('AgProductionTechnology'):
#            root3 = et.Element('root')
#            root3=(tech)
#            for yr in root3.iter('period'):
#                root4 = et.Element('root')
#                root4=yr
#                for gas in root4.iter('Non-CO2'):
#                    root5 = et.Element('root')
#                    root5=gas



for x in xmldoc.iter('resultWrapper'):
    root1=ET.Element('xmldoc')
    root1=x
    for result in root1.iter('resultList'):
        root2=ET.Element('root')
        print(result)




#trying with rdflib here... 
#rdfData=rdflib.graph()
#n3=rdfData.parse(dcurl, format='application/rdf+xml')
#import zeep
#from zeep import Client, Settings
#settings = Settings(strict=False, xml_huge_tree=True)
#client = Client('https://www.ebi.ac.uk/europepmc/webservices/soap?wsdl', settings=settings)

#st.write(client.settings)
