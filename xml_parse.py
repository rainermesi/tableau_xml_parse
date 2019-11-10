# import libs
import os
import xml.etree.ElementTree as ET
import pandas

# get and parse xml
tree = ET.parse('b2b_loyalty.xml')
root = tree.getroot()

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

#cant join, columns in int64/str format
joined_df = pandas.DataFrame.join(cn_df,cm_df, on='colname', how='left' )

# ToDo: 
# * Should add more columns to colnames (might be valuable)
# * refactor into a function
# * test on other datasets
# * add datasource column
