from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPerson

class PersonContent(Container):
    """Person Content
    """
    implements(IPerson,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Person"

    position = FieldProperty(IPerson['position'])
    email = FieldProperty(IPerson['email'])
    telephone = FieldProperty(IPerson['telephone'])
    fax = FieldProperty(IPerson['fax'])
    office = FieldProperty(IPerson['office'])
    misc = FieldProperty(IPerson['misc'])

factory = Factory(
        PersonContent,
        )
