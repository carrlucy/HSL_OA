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
searchThis=st.sidebar.text_input('data')

#https://www.foxinfotech.in/2019/04/python-how-to-read-xml-from-url.html
restQuery=urlopen('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='searchThis'&resultType=core&cursorMark=*&pageSize=35&format=xml')
xmlTree=ET.parse(restQuery)
root = xmlTree.getroot()


#st.write(root[4][0][0].text)    
#https://towardsdatascience.com/converting-multi-layered-xml-files-to-dataframes-in-python-using-xmltree-a13f9b043b48
#for a in root[4]:
#    st.write(a.text)


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
    
    


#for x in xmldoc.iter('resultList'):
    #root1=ET.Element('xmldoc')
   #root1=x
    #st.write("hello")
    #for x2 in root1.iter('result'):
       # root2=ET.Element('xmldoc')
        #st.write(x2.)

#DOI=[]
#AuthorFullName=[]
#AuthorAffiliation=[]

#for x in tree.iter('result'):
#    root1=tree.Element('root')
#    root1=x
#    for writer in root1.iter('author'):
#        root2 = et.Element('root')
#        st.write(writer)
#        root2=(writer)
#        for authorInstitution in root2.iter('authorAffiliation'):
#            root3 = et.Element('root')
#           st.write(authorInstitution)
#            root3=authorInstitution
#            for authorInstitution in root4.iter('authorAffiliation'):
#                DOI.append(result.attrib['doi'])
#                AuthorFullName.append(writer.attrib['fullName'])
#                AuthorAffiliation.append(authorInstitution.attrib['affiliation'])
#df = pd.DataFrame({'DOI': 
#DOI,'AuthorFullName':AuthorFullName,'AuthorAffiliation':AuthorAffiliation })
                        
                
# This is also talks about using the API with Python, starting on slide 23 https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/wp-content/uploads/sites/128/2020/11/Webinar-slides-Europe-PMC-programmatically_2020.pdf



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


        
#trying with rdflib here... 
#rdfData=rdflib.graph()
#n3=rdfData.parse(dcurl, format='application/rdf+xml')
#import zeep
#from zeep import Client, Settings
#settings = Settings(strict=False, xml_huge_tree=True)
#client = Client('https://www.ebi.ac.uk/europepmc/webservices/soap?wsdl', settings=settings)

#st.write(client.settings)
