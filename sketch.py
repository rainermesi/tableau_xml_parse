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

####################################################################

for column in root.iter('column'):
    colnames['colname'].append(column.attrib['name'])
    #colnames['caption'].append(column.attrib['caption'])
    colnames['datatype'].append(column.attrib['datatype'])
    #colnames['param-domain-type'].append(column.attrib['param-domain-type'])
    colnames['role'].append(column.attrib['role'])
    #colnames['type'].append(column.attrib['type'])
    #colnames['value'].append(column.attrib['value'])
    for i in column:
        if i.attrib == {}:
            colmeta['colname'].append(column.attrib['name'])
            colmeta['class'].append('not applicable')
            colmeta['formula'].append('not applicable')
        else:
            colmeta['colname'].append(column.attrib['name'])
            colmeta['class'].append(i.attrib['class'])
            colmeta['formula'].append(i.attrib['formula'])