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

    staff = FieldProperty(IResearchProject['staff'])

factory = Factory(
        ResearchProjectContent,
        )
