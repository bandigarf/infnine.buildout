from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPublicationListing

class PublicationListingContent(Item):
    """Page to list Chair Publications
    """
    implements(IPublicationListing,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Publication Listing"

factory = Factory(
        PublicationListingContent,
        )
