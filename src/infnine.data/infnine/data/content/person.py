from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPerson

from infnine.data.common import authors_list, filterNamesUrl, filterNamesUmlaut, authors, filtered_name

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
    telephone1 = FieldProperty(IPerson['telephone1'])
    fax = FieldProperty(IPerson['fax'])
    office = FieldProperty(IPerson['office'])
    office1 = FieldProperty(IPerson['office1'])
    introduction = FieldProperty(IPerson['introduction'])
    research_topics = FieldProperty(IPerson['research_topics'])
    research_projects_current = FieldProperty(IPerson['research_projects_current'])
    research_projects_former = FieldProperty(IPerson['research_projects_former'])
    teaching = FieldProperty(IPerson['teaching'])
    teaching_misc = FieldProperty(IPerson['teaching_misc'])
    students = FieldProperty(IPerson['students'])
    misc = FieldProperty(IPerson['misc'])
    publications = FieldProperty(IPerson['publications'])
    show_link_all_publications = FieldProperty(IPerson['show_link_all_publications'])
    show_link_teaching = FieldProperty(IPerson['show_link_teaching'])

    author_list = authors_list
    fN = filterNamesUrl
    fNU = filterNamesUmlaut
    auth = authors
    filtered_name = filtered_name

factory = Factory(
        PersonContent,
        )
