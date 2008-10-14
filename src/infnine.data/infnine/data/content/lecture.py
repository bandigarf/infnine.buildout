from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import ILecture

class LectureContent(Container):
    """Lecture Content
    """
    implements(ILecture,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Lecture"

factory = Factory(
        LectureContent,
        )
