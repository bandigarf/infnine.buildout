from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IResearchProject

class ResearchProjectContent(Container):
    """Research Project Content
    """
    implements(IResearchProject,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Research Project"

    team = FieldProperty(IResearchProject['team'])
    project_details = FieldProperty(IResearchProject['project_details'])
    publications = FieldProperty(IResearchProject['publications'])

factory = Factory(
        ResearchProjectContent,
        )
