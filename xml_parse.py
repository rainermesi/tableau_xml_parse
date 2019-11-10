import os
import xml.etree.ElementTree as ET
import pandas

#setwd

os.chdir('C:\\Users\\raine\\Google Drive\\DATA\\Tableau DataSource')
os.getcwd()
os.listdir()

#parse xml

tree = ET.parse('b2b_loyalty.xml')

root = tree.getroot()
    
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

#########################################################################
## DEBUG START
#########################################################################

# debug for statement to return formulas
# create variables for saving

colnames = {
    'colname': []
}

colmeta = {
    'colname': [],
    'class': [],
    'formula': []
}

# get column names and formulas
for column in root.iter('column'):
    colnames['colname'].append(column.attrib['name'])
    for i in column:
        if i.attrib == {}:
            colmeta['colname'].append(column.attrib['name'])
            colmeta['class'].append('null')
            colmeta['formula'].append('null')
        else:
            colmeta['colname'].append(column.attrib['name'])
            colmeta['class'].append(i.attrib['class'])
            colmeta['formula'].append(i.attrib['formula'])

# create dataframes
cn_df = pandas.DataFrame(colnames)
cm_df = pandas.DataFrame(colmeta)

# ToDo: 
# * Should add more columns to colnames (might be valuable)
# * refactor into a function
# * test on other datasets
# * add datasource column
