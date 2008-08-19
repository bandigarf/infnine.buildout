from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IResearchPage

class ResearchPageContent(Item):
    """Page to list research projects
    """
    implements(IResearchPage,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Research Page"

    description = FieldProperty(IResearchPage['description'])

factory = Factory(
        ResearchPageContent,
        )
