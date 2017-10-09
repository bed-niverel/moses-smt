#!/usr/bin/python2
# Dumps the content in given language of the given tmx files to stdout


import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 3:
    print 'Usage ./tmx2moses filename lang'
    exit()

filename = str(sys.argv[1])
lang = str(sys.argv[2])

tree = ET.parse(filename)
root = tree.getroot()

tagname = '{http://www.w3.org/XML/1998/namespace}lang'


for tu in root.iter('tu'):
    doexport = True
    strings = {}
    for tuv in tu.iter('tuv'):
        seg = tuv.find('seg')
        string = seg.text
        if string and len(string) > 1:
            langcode = tuv.get(tagname)
            strings[langcode] = string.encode('utf-8').strip()
        else:
            doexport = False
    if doexport:
        #print 'a'
        print strings[lang].replace("\n", "")
