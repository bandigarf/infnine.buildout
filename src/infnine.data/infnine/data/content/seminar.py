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

    title_english = FieldProperty(ISeminar['title_english'])
    seminar_type = FieldProperty(ISeminar['seminar_type'])
    professor = FieldProperty(ISeminar['professor'])
    instructor = FieldProperty(ISeminar['instructor'])
    date_place = FieldProperty(ISeminar['date_place'])
    seminar_language = FieldProperty(ISeminar['seminar_language'])
    module = FieldProperty(ISeminar['module'])
    term = FieldProperty(ISeminar['term'])
    url = FieldProperty(ISeminar['url'])
    body = FieldProperty(ISeminar['body'])

factory = Factory(
        SeminarContent,
        )
