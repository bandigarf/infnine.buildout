""" A script to convert .bib files to Zope objects
"""
import sys
def filtered_pubtype(string):
    string = string.replace('Refereed', '')
    string = string.replace('Award Winner', '')
    string = string.strip(' ,')

    if string in ['Journal', 'Workshop Paper', 'Conference Paper', 'Book', 'Book Chapter']:
        return string + 's'

    if string == 'PhD Thesis':
        return 'PhD Theses'

    return string

def bib2zope(filename, app = None):
    import _bibtex
    file = _bibtex.open_file(filename, True)
    entry = _bibtex.next(file)
    while entry != None:
        keys = entry[4].keys()
        id = entry[0]
        pubtype = entry[1]
        print '-----'
        print 'id:', id
        print 'pubype:', pubtype
        print 'keys:', keys
        for key in keys:
            print key, ':', _bibtex.get_native(entry[4][key]).strip('{} ')

        if app != None:
            publications = app.infnine.publications
            print "Running in Zope, creating objects in ZODB..."
            if not publications.hasObject(id):
                print "Entry", id, "not yet in ZODB, creating"
                admin = app.acl_users.getUser('admin')
                import AccessControl
                AccessControl.SecurityManagement.newSecurityManager(None, admin)
                from Testing.makerequest import makerequest
                app = makerequest(app)
                publications.invokeFactory('Publication', id)
            pub = publications.__getitem__(id)

            print "Updating", id, keys
            from infnine.data.interfaces import IPublication
            for key in keys:
                if not key.replace('-', '_') in (IPublication._v_attrs.keys()):
                    print "!!! Missing key:", key

                value = _bibtex.get_native(entry[4][key]).strip('{} "')

                if key in ['year']:
                    value = int(value)
                elif key == 'bib2html_pubtype':
                   value = unicode(filtered_pubtype(value))
                else:
                    value = unicode(value)

                if '-' in key:
                    pub.__setattr__(key.replace('-', '_'), value)
                else:
                    pub.__setattr__(key, value)

            pub.reindexObject()
            import transaction
            transaction.commit()

        entry = _bibtex.next(file)

# main code goes here

print 'bib2zope script'
print '---------------'

bibpath = './'

import os

user = os.popen('whoami').read().strip()
if user == 'infnine':
    bibpath = '/usr/proj/infnine/infninebib/bibliography/'

if user == 'andrija':
    bibpath = '/home/andrija/projects/tum/iasdocs/'

if user == 'pangercic':
    bibpath = '/home/pangercic/research/iasdoc/bibliography/'

all_files = os.listdir(bibpath)
bib_files_ias = [file for file in all_files if (file[-4:] == '.bib' and (file[0:15] == 'iaspublications'))]
bib_files_iu = [file for file in all_files if (file[-4:] == '.bib' and (file[0:14] == 'iupublications'))]
bib_files_mqm = [file for file in all_files if (file[-4:] == '.bib' and (file[0:3] == 'Mqm'))]
bib_files_iu.sort()
bib_files_mqm.sort()
bib_files_ias.sort()
bib_files_ias += bib_files_mqm
bib_files_ias += bib_files_iu
print "Found .bib files:", bib_files_ias
#sys.exit(0)
if not 'app' in dir():
    app = None

for file in bib_files_ias:
    bib2zope(bibpath + file, app)
