from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPublicationListing

from infnine.data.common import authors_list, filterNamesUrl, filterNamesUmlaut

class PublicationListingContent(Item):
    """Page to list Chair Publications
    """
    implements(IPublicationListing,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Publication Listing"

    author_list = authors_list
    fN = filterNamesUrl
    fNU = filterNamesUmlaut

factory = Factory(
        PublicationListingContent,
        )


