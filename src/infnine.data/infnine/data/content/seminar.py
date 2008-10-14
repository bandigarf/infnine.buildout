from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import ISeminar

class SeminarContent(Container):
    """Seminar Content
    """
    implements(ISeminar,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Seminar"

factory = Factory(
        SeminarContent,
        )
