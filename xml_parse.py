import os
import xml.etree.ElementTree as ET
import pandas

#setwd

os.chdir('C:\\Users\\Rainer\\Google Drive\\DATA\\Tableau DataSource')
os.getcwd()
os.listdir()

#parse xml

tree = ET.parse('b2b_loyalty.xml')

root = tree.getroot()

#print(root.tag)
 #print(root.attrib)
#
#for child in root:
#    print(child.tag, child.attrib)
#    
#for child in root:
##    print(child.tag)    
##    
##print(child[1].tag, child[1].attrib)
##
##for calculation in root.iter('column'):
##    print(calculation.attrib)
##    print('---------------------------------------')
##    
##for child in root:
##    for calculation_ in child.iter('calculation'):
##        print(calculation_.attrib)
##        print('---')      
##
###1st try to get useful stuff out of xml
##
#for column in root.iter('column'):
##    print('NAME:')
##    print(column.attrib['name'])
#    print(column.attrib)
##    for calculation in column.iter('x'):
##        print('FORMULA:')
##        print(calculation.attrib)
##        print('***********')
#for i in root.iter():
#    print(i)
##2nd iteration
        
#        
#for column in root.iter('column'):
#    #print('NAME:')
#    #caption1 = column.attrib['caption']
#    print('name',column.attrib['name'])
#    if 'caption' in column.attrib:
#        print('caption:',column.attrib['caption'])
#    else:
#        print('caption: no caption')
#    #print(column.attrib['caption'])
#    print('role:',column.attrib['role'])
#    print('datatype',column.attrib['datatype'])
#    #print(column.attrib)
#    for calculation in column.iter('calculation'):
#        print('formula:',calculation.attrib['formula'])
#        #print('***********')
#    print('----------------------------------------------------')
    
#3rd iteration
    
#create dictionary to hold values
    
fields = {
        'name': [],
        'caption': [],
        'role': [],
        'datatype': [],
        'formula': []
        }

#fields['name'].append('me')

for column in root.iter('column'):
    fields['name'].append(column.attrib['name'])
    if 'caption' in column.attrib:
        fields['caption'].append(column.attrib['caption'])
    else:
        fields['caption'].append('no caption')
    fields['role'].append(column.attrib['role'])
    fields['datatype'].append(column.attrib['datatype'])
    if 'formula' in column.attrib:
        for calculation in column.iter('calculation'):
            fields['formula'].append(calculation.attrib['formula'])
    else: fields['formula'].append('!not a calculated field!')

#if statemetn does not work, always returns else
        
fields_df = pandas.DataFrame(fields)

fields_df.head()

fields_df.to_csv('parse_result.txt', sep = '|')