"""
"""

from zope.i18nmessageid import MessageFactory

from Products.CMFCore.permissions import setDefaultRoles

_ = MessageFactory('infnine.data')

setDefaultRoles('Infnine Data: Add First Page', ('Manager',))
setDefaultRoles('Infnine Data: Add Group', ('Manager',))
setDefaultRoles('Infnine Data: Add Person', ('Manager',))
setDefaultRoles('Infnine Data: Add Publication', ('Manager',))
setDefaultRoles('Infnine Data: Add Research Project', ('Manager',))
setDefaultRoles('Infnine Data: Add Alumni Page', ('Manager',))
setDefaultRoles('Infnine Data: Add Application Domain', ('Manager',))
setDefaultRoles('Infnine Data: Add People Page', ('Manager',))
setDefaultRoles('Infnine Data: Add Publication Listing', ('Manager',))
setDefaultRoles('Infnine Data: Add Research Page', ('Manager',))
setDefaultRoles('Infnine Data: Add Student Project', ('Manager',))
setDefaultRoles('Infnine Data: Add Student Project Listing', ('Manager',))
setDefaultRoles('Infnine Data: Add Lecture', ('Manager',))
setDefaultRoles('Infnine Data: Add Practical Course', ('Manager',))
setDefaultRoles('Infnine Data: Add Seminar', ('Manager',))

def initialize(context):
    """Initializer called when used as a Zope 2 product.
    """
    pass
