# * mus3asis colnames error, why?
# * add into TkInter 
# * input and output selectable
# * add ability to loop through multiple xml files and append into single datasource



import os
import xml.etree.ElementTree as ET
import pandas

def xml_parse(xmlfile):
    col_names = {
        'colname': [],
        'datatype': [],
        'role': []
    }
    col_meta = {
        'colname': [],
        'class': [],
        'formula': []
    }
    data_meta = {
        'remote-name': [],
        'local-name': [],
        'parent-name': [],
    }

    xmlroot = ET.parse(xmlfile).getroot()
    xmliterator = xmlroot.getiterator()

    for column in xmlroot.iter('column'):
        col_names['colname'].append(column.attrib['name'])
        col_names['datatype'].append(column.attrib['datatype'])
        col_names['role'].append(column.attrib['role'])
        for i in column:
            if i.attrib == {}:
                col_meta['colname'].append(column.attrib['name'])
                col_meta['class'].append('not applicable')
                col_meta['formula'].append('not applicable')
            else:
                col_meta['colname'].append(column.attrib['name'])
                col_meta['class'].append(i.attrib['class'])
                col_meta['formula'].append(i.attrib['formula'])

    for element in xmliterator:
        if element.tag == 'metadata-record':
            if list(element):
                for child in element:
                    if child.tag == 'remote-name':
                        data_meta['remote-name'].append(child.text)
                    if child.tag == 'local-name':
                        data_meta['local-name'].append(child.text)
                    if child.tag == 'parent-name':
                        data_meta['parent-name'].append(child.text)

    pandas.DataFrame(col_names).merge(pandas.DataFrame(col_meta), on='colname', how='left' ).to_csv(r'C:\Users\raine\Google Drive\DATA\Tableau DataSource\columns.csv')
    pandas.DataFrame(data_meta).to_csv(r'C:\Users\raine\Google Drive\DATA\Tableau DataSource\metadata.csv')

xml_parse(r'C:\Users\raine\Google Drive\DATA\Tableau DataSource\Transactional_NPS.xml')
