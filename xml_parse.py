# import libs
import os
import xml.etree.ElementTree as ET
import pandas

# get and parse xml
tree = ET.parse('b2b_loyalty.xml')
root = tree.getroot()

# print full xml structure

iter = root.getiterator()

for element in iter:
    print("Element:", element.tag)
    if element.keys():
        print("\tAttributes:")
        for name, value in element.items():
            print("\t\tName: '%s'"%(name))
    print("\tChildren")
    if element.text:
        text = element.text
        text = len(text) > 40 and text[:40]+ "..." or text
        print("\t\tText:", repr(text))
    if element.getchildren():
        for child in element:
            print("\t\tElement", child.tag, ":", child.text)
        if child.tail:
            text = child.tail
            text = len(text) > 40 and text[:40] + "..." or text
            print("t\tText:", repr(text))

# print only metadata elements

for element in iter:
    if element.tag == 'metadata-record':
        print("Element:", element.tag)
        if element.keys():
            print("\tAttributes:")
            for name, value in element.items():
                print("\t\tName: '%s', Value: '%s'"%(name, value))
        print("\tChildren")
        if element.text:
            text = element.text
            text = len(text) > 40 and text[:40]+ "..." or text
            print("\t\tText:", repr(text))
        if element.getchildren():
            for child in element:
                print("\t\tElement", child.tag, ":", child.text)
            if child.tail:
                text = child.tail
                text = len(text) > 40 and text[:40] + "..." or text
                print("t\tText:", repr(text))

#########################################################################
## DEBUG START
#########################################################################

# debug for statement to return formulas
# create variables for saving

colnames = {
    'colname': [],
    'datatype': [],
    'role': []
}

colmeta = {
    'colname': [],
    'class': [],
    'formula': []
}

# get column names and formulas
for column in root.iter('column'):
    colnames['colname'].append(column.attrib['name'])
    colnames['datatype'].append(column.attrib['datatype'])
    colnames['role'].append(column.attrib['role'])
    for i in column:
        if i.attrib == {}:
            colmeta['colname'].append(column.attrib['name'])
            colmeta['class'].append('not applicable')
            colmeta['formula'].append('not applicable')
        else:
            colmeta['colname'].append(column.attrib['name'])
            colmeta['class'].append(i.attrib['class'])
            colmeta['formula'].append(i.attrib['formula'])

# create dataframes
cn_df = pandas.DataFrame(colnames)
cm_df = pandas.DataFrame(colmeta)

#use merge instead of join
joined_df = cn_df.merge(cm_df, on='colname', how='left' )

# add datasource column(s) and other info found in the metadata element

iter_2 = root.getiterator()

elem_meta = {
    'remote-name': [],
    'local-name': [],
    'parent-name': [],
}

for element in iter_2:
    if element.tag == 'metadata-record':
        if element.getchildren():
            for child in element:
                if child.tag == 'remote-name':
                    elem_meta['remote-name'].append(child.text)
                if child.tag == 'local-name':
                    elem_meta['local-name'].append(child.text)
                if child.tag == 'parent-name':
                    elem_meta['parent-name'].append(child.text)

em_df = pandas.DataFrame(elem_meta)

# ToDo: 
# X Should add more columns to colnames (might be valuable)
# * refactor into a function
# * test on other datasets
# * add datasource column