#!/usr/bin/env python

def bibsplit(multi_entry_file):
    mef = file(multi_entry_file, 'r').readlines()
    for l in mef:
        if l[0] == '@':
            id = l.rstrip(' \n,')[l.find('{')+1:]
            print 'Found entry:', id
            sef = file(output_dir + id + '.bib', 'w')
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
bib_files = [bib_file for bib_file in all_files if (bib_file[-4:] == '.bib' and bib_file[-11:] != "private.bib" and bib_file[-10:] != "latex8.bib" and bib_file[0:12] != "bibliography" and bib_file[0:12] != "aspogamo.bib")]
print "Found .bib files:", bib_files

for multi_entry_file in bib_files:
    bibsplit(multi_entry_file)

