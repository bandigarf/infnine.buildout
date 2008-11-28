from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPracticalCourse

class PracticalCourseContent(Container):
    """Practical Course Content
    """
    implements(IPracticalCourse,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Practical Course"

    title_german = FieldProperty(IPracticalCourse['title_german'])
    details = FieldProperty(IPracticalCourse['details'])
    practicalcourse_type = FieldProperty(IPracticalCourse['practicalcourse_type'])
    professor = FieldProperty(IPracticalCourse['professor'])
    instructor = FieldProperty(IPracticalCourse['instructor'])
    date_place = FieldProperty(IPracticalCourse['date_place'])
    practicalcourse_language = FieldProperty(IPracticalCourse['practicalcourse_language'])
    modul = FieldProperty(IPracticalCourse['modul'])
    term = FieldProperty(IPracticalCourse['term'])
    url = FieldProperty(IPracticalCourse['url'])
    body = FieldProperty(IPracticalCourse['body'])

factory = Factory(
        PracticalCourseContent,
        )
