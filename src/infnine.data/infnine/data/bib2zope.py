""" A script to convert .bib files to Zope objects
"""

def bib2zope(filename, app = None):
    import _bibtex
    file = _bibtex.open_file(bibpath + '/' + filename, True)
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
            print "Running in Zope, creating objects in ZODB..."
            if not app.infnine.stuff.hasObject(id):
                print "Entry", id, "not yet in ZODB, creating"
                admin = app.acl_users.getUser('admin')
                import AccessControl
                AccessControl.SecurityManagement.newSecurityManager(None, admin)
                from Testing.makerequest import makerequest
                app = makerequest(app)
                app.infnine.stuff.invokeFactory('Publication', id)
            pub = app.infnine.stuff.__getitem__(id)

            print "Updating", id, keys
            from infnine.data.interfaces import IPublication
            for key in keys:
                if not key in (IPublication._v_attrs.keys() + ['citeulike-article-id']):
                    print "!!! Missing key:", key

                value = _bibtex.get_native(entry[4][key]).strip('{} ')

                if key in ['year']:
                    value = int(value)
                else:
                    value = unicode(value)

                if key in ['citeulike-article-id']:
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
all_files = os.listdir(bibpath)
bib_files = [file for file in all_files if file[-4:] == '.bib']
print "Found .bib files:", bib_files

if not 'app' in dir():
    app = None

for file in bib_files:
#    bibfile2zopeobject(file)
    bib2zope(file, app)
