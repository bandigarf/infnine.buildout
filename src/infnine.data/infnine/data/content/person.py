from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPerson

class PersonContent(Container):
    """Person Content
    """
    implements(IPerson,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Person"

    status = FieldProperty(IPerson['status'])
    alumni_date = FieldProperty(IPerson['alumni_date'])
    position = FieldProperty(IPerson['position'])
    department = FieldProperty(IPerson['department'])
    email = FieldProperty(IPerson['email'])
    telephone = FieldProperty(IPerson['telephone'])
    fax = FieldProperty(IPerson['fax'])
    office = FieldProperty(IPerson['office'])
    introduction = FieldProperty(IPerson['introduction'])
    publications = FieldProperty(IPerson['publications'])
    research_projects_current = FieldProperty(IPerson['research_projects_current'])
    research_projects_former = FieldProperty(IPerson['research_projects_former'])
    teaching = FieldProperty(IPerson['teaching'])
    students = FieldProperty(IPerson['students'])
    misc = FieldProperty(IPerson['misc'])

factory = Factory(
        PersonContent,
        )
