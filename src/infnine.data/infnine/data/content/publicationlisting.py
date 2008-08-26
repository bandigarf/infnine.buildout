from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPublicationListing

from infnine.data.common import authors_list

class PublicationListingContent(Container):
    """Page to list Chair Publications
    """
    implements(IPublicationListing,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Publication Listing"
    author_list = authors_list


factory = Factory(
        PublicationListingContent,
        )
