import zope.interface
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IContact, IContact2
from plone.app.content.container import Container
from zope.component.factory import Factory

class Contact(Container):
    """See ``zcontact.interfaces.IContact``."""
    zope.interface.implements(IContact)

    firstName = FieldProperty(IContact['firstName'])
    lastName = FieldProperty(IContact['lastName'])


factory = Factory(
        Contact
        )


class Contact2(Container):
    """See ``zcontact.interfaces.IContact``."""
    zope.interface.implements(IContact2)

    firstName = FieldProperty(IContact2['firstName'])
    lastName = FieldProperty(IContact2['lastName'])


factory = Factory(
        Contact
        )
