from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPublication

class PublicationContent(Container):
    """Publication Content
    """
    implements(IPublication,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Publication"

#    title = FieldProperty(IPublication['title'])

factory = Factory(
        PublicationContent,
        )
