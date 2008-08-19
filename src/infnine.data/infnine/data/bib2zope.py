""" A script to convert .bib files to Zope objects
"""

def bibfile2zopeobject(file):
    print "File:", file
    f = open(bibpath + '/' + file)
    bibtex = ''
    for line in f.readlines():
        bibtex += line

    # bibtex files contain multiple entries!
    bib_dict = parseBibTeX(bibtex)
    for entry_id in bib_dict.keys():
        createZopePublication(app, entry_id, bib_dict[entry_id])

def createZopePublication(app, id, entry_dict):
    if not app.infnine.stuff.hasObject(id):
        print "Entry", id, "not yet in ZODB, creating"
        admin = app.acl_users.getUser('admin')
        import AccessControl
        AccessControl.SecurityManagement.newSecurityManager(None, admin)
        from Testing.makerequest import makerequest
        app = makerequest(app)
        app.infnine.stuff.invokeFactory('Publication', id)

    print "Updating field values for", id
    pub = app.infnine.stuff.__getitem__(id)
    pub.title = entry_dict['title']

    pub.reindexObject()
    import transaction
    transaction.commit()

def parseBibTeX(bibtex):
    # Dominik's function for parsing BibTeX entries
    import re
    bibtex = (bibtex + "@").replace("@", "@@") # make sure that all entries have "@" as an ending delimiter (and make sure that patterns are non-overlapping)
    entries = re.findall(r'@[A-Za-z]+\s*\{(.*?)\}\s*@', bibtex, re.DOTALL | re.MULTILINE)
    delims = [['"', '"'], ["\\{", "\\}"]]
    ret = {}
    for entry in entries:
        id = re.match("\w+", entry).group(0)
        l = []
        for delim in delims:
            l.extend(re.findall(r'([a-z]+)\s*=\s*%s(.*?)%s' % (delim[0], delim[1]), entry))
        ret[id] = dict(map(lambda x: (x[0], x[1].strip("{}").strip()), l))
    return ret


# main code goes here

print 'bib2zope script'
print '---------------'

bibpath = './'

import os
all_files = os.listdir(bibpath)
bib_files = [file for file in all_files if file[-4:] == '.bib']
print "Found .bib files:", bib_files

for file in bib_files:
    bibfile2zopeobject(file)
