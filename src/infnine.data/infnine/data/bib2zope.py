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

    print "Updating", id, entry_dict.keys()
    pub = app.infnine.stuff.__getitem__(id)

    pub.title = entry_dict['title']

    if 'pubtype' in entry_dict.keys():
        pub.pubtype = unicode(entry_dict['pubtype'])

    if 'author' in entry_dict.keys():
        pub.author = unicode(entry_dict['author'])

    if 'funding' in entry_dict.keys():
        pub.funded_by = unicode(entry_dict['funding'])

    if 'journal' in entry_dict.keys():
        pub.journal = unicode(entry_dict['journal'])

    if 'booktitle' in entry_dict.keys():
        pub.booktitle = unicode(entry_dict['booktitle'])

    if 'year' in entry_dict.keys():
        pub.year = int(entry_dict['year'])

    if 'note' in entry_dict.keys():
        pub.note = unicode(entry_dict['note'])

    if 'abstract' in entry_dict.keys():
        pub.abstract = unicode(entry_dict['abstract'])

    if 'groups' in entry_dict.keys():
        pub.groups = unicode(entry_dict['groups'])

    if 'rescat' in entry_dict.keys():
        pub.rescat = unicode(entry_dict['rescat'])

#    bibtex_entry = ''

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
