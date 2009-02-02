from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import ISemester

class SemesterContent(Container):
    """Semester Content
    """
    implements(ISemester,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Semester"

factory = Factory(
        SemesterContent,
        )
