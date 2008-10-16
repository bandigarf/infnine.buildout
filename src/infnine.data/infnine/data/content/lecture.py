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

    title_german = FieldProperty(ILecture['title_german'])
    details = FieldProperty(ILecture['details'])
    lecture_type = FieldProperty(ILecture['lecture_type'])
    professor = FieldProperty(ILecture['professor'])
    instructor = FieldProperty(ILecture['instructor'])
    date_place = FieldProperty(ILecture['date_place'])
    language = FieldProperty(ILecture['language'])
    modul = FieldProperty(ILecture['modul'])
    term = FieldProperty(ILecture['term'])

factory = Factory(
        LectureContent,
        )