from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IResearchProject

from infnine.data.common import authors_list, filterNamesUrl, filterNamesUmlaut,authors

class ResearchProjectContent(Container):
    """Research Project Content
    """
    implements(IResearchProject,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Research Project"

    summary = FieldProperty(IResearchProject['summary'])
    research_topics = FieldProperty(IResearchProject['research_topics'])
    application_domain = FieldProperty(IResearchProject['application_domain'])
    team = FieldProperty(IResearchProject['team'])
    former_personell = FieldProperty(IResearchProject['former_personell'])
    project_details = FieldProperty(IResearchProject['project_details'])
    publications = FieldProperty(IResearchProject['publications'])

    author_list = authors_list
    fN = filterNamesUrl
    fNU = filterNamesUmlaut
    auth = authors

factory = Factory(
        ResearchProjectContent,
        )
