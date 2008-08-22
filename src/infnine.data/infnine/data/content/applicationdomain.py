from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IApplicationDomain

class ApplicationDomainContent(Item):
    """Application Domain Content
    """
    implements(IApplicationDomain,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Application Domain"

    details = FieldProperty(IApplicationDomain['details'])

factory = Factory(
        ApplicationDomainContent,
        )
