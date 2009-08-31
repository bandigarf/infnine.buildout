# Memberdata export script for Plone 3.0
#
# based on:
#    http://transcyberia.info/archives/23-howto-sync-mailman-from-plone.html
#    http://www.zopelabs.com/cookbook/1140753093
#    http://plone.org/documentation/how-to/export-member-data-to-csv
#
# desc:
#    None of the scripts above can extract password hashes on Plone3.0, 
#    BUT THIS ONE CAN!!!
#
#    Execute this as normal External Script, and DON'T make it public accessible 
#    (unless you don't mind people having your hashes). You have been warned. 
#    Have fun (^,^)
#
#See: http://plone.org/documentation/how-to/create-and-use-an-external-method
#on how to integrate an External Method into Plone page
from zope.component import getSiteManager
from StringIO import StringIO
import csv
import time

def getMembersCSV(self):

    request = self.REQUEST
    text = StringIO()
    writer = csv.writer(text)
    portalRoot = getSiteManager()
    people_list = portalRoot.people.getChildNodes()
    
    properties = ['title',
                        'status',
                        'email',
                        'telephone',
                        'office',
                        'position',
                        'fax']

    writer.writerow(properties)

    for person in range(people_list.__len__()):
        row = []
        row.append(people_list._data[person].title)
        row.append(people_list._data[person].status)
        row.append(people_list._data[person].email)
        row.append(people_list._data[person].telephone)
        row.append(people_list._data[person].office)
        row.append(people_list._data[person].position)
        row.append(people_list._data[person].fax)
        writer.writerow(row)


    request.RESPONSE.setHeader('Content-Type','application/csv')
    request.RESPONSE.setHeader('Content-Length',len(text.getvalue()))
    request.RESPONSE.setHeader('Content-Disposition',
                               'inline;filename=members-%s.csv' %
                               time.strftime("%Y%m%d-%H%M%S",time.localtime()))

    return text.getvalue()
