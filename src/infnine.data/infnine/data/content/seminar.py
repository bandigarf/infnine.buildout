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

    title_german = FieldProperty(ISeminar['title_german'])
    details = FieldProperty(ISeminar['details'])
    seminar_type = FieldProperty(ISeminar['seminar_type'])
    professor = FieldProperty(ISeminar['professor'])
    instructor = FieldProperty(ISeminar['instructor'])
    date_place = FieldProperty(ISeminar['date_place'])
    language = FieldProperty(ISeminar['language'])
    modul = FieldProperty(ISeminar['modul'])
    term = FieldProperty(ISeminar['term'])

factory = Factory(
        SeminarContent,
        )
