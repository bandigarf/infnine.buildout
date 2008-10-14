from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IStudentProjectListing

class StudentProjectListingContent(Item):
    """Page to list student projects
    """
    implements(IStudentProjectListing,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Student Project Listing"

factory = Factory(
        StudentProjectListingContent,
        )
