#!/usr/bin/env python

from string import whitespace

def bibsplit(multi_entry_file):
    mef = file(multi_entry_file, 'r').readlines()
    sef = None
    for l in mef:
        if l[0] == '@':
            id = l[l.find('{')+1:].strip().strip(whitespace + ',;')
            print 'Found entry:', id
            sef = file(output_dir + id + '.bib', 'w')
        if sef != None:
            sef.write(l)

print 'bibsplitter script'
print '------------------'

bibpath = './'
output_dir = './'

import os

user = os.popen('whoami').read().strip()
if user == 'infnine':
    bibpath = '/usr/proj/infnine/infninebib/bibliography/'
    output_dir = '/usr/proj/infnine/infninebib/infninebib/'

all_files = os.listdir(bibpath)
bib_files = [bib_file for bib_file in all_files if (bib_file[-4:] == '.bib' and (bib_file[0:15] == 'iaspublications' or bib_file[0:14] == 'iupublications'))]
print "Found .bib files:", bib_files

for multi_entry_file in bib_files:
    bibsplit(bibpath + multi_entry_file)

