from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IFirstPage

class FirstPageContent(Item):
    """First page
    """
    implements(IFirstPage,
            ITTWLockable,
            INameFromTitle)

    portal_type = "First Page"

factory = Factory(
        FirstPageContent,
        )
