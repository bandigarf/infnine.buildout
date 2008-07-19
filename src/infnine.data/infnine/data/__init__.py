"""
"""

from zope.i18nmessageid import MessageFactory

from Products.CMFCore.permissions import setDefaultRoles

_ = MessageFactory('infnine.data')

setDefaultRoles('Infnine Data: Add Person', ('Manager',))
setDefaultRoles('Infnine Data: Add Publication', ('Manager',))

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
