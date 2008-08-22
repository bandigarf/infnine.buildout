from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IAlumniPage

class AlumniPageContent(Item):
    """Page to list alumni
    """
    implements(IAlumniPage,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Alumni Page"

factory = Factory(
        AlumniPageContent,
        )
