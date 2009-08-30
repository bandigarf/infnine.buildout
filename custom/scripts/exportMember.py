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

from StringIO import StringIO
import csv
import time

def getMembersCSV(self):

    request = self.REQUEST
    text = StringIO()
    writer = csv.writer(text)

    # core properties (username/password)
    core_properties = ['member_id','password']

    # extra portal_memberdata properties
    extra_properties = ['title',
                        'status',
                        'email',
                        'telephone',
                        'office',
                        'position',
                        'fax']

    properties = core_properties + extra_properties

    writer.writerow(properties)

    membership=self.portal_membership
    passwdlist=self.acl_users.source_users._user_passwords

    for memberId in membership.listMemberIds():
        row = []
        for property in properties:
            if property == 'member_id':
               row.append(memberId)
            elif property == 'password':
               row.append(passwdlist[memberId])
            else:
               member = membership.getMemberById(memberId)
               row.append(member.getProperty(property))

        writer.writerow(row)


    request.RESPONSE.setHeader('Content-Type','application/csv')
    request.RESPONSE.setHeader('Content-Length',len(text.getvalue()))
    request.RESPONSE.setHeader('Content-Disposition',
                               'inline;filename=members-%s.csv' %
                               time.strftime("%Y%m%d-%H%M%S",time.localtime()))

    return text.getvalue()
