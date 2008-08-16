from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IGroup

class GroupContent(Container):
    """Group Content
    """
    implements(IGroup,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Group"

    summary = FieldProperty(IGroup['summary'])
    research_topic = FieldProperty(IGroup['research_topic'])
    application_domain = FieldProperty(IGroup['application_domain'])
    team = FieldProperty(IGroup['team'])
    former_personell = FieldProperty(IGroup['former_personell'])
    group_details = FieldProperty(IGroup['group_details'])
    publications = FieldProperty(IGroup['publications'])

factory = Factory(
        GroupContent,
        )
