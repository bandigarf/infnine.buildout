from zope.interface import Interface
from zope.schema import TextLine, Text, Choice, Int

class IGroup(Interface):
    """A group
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the group",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the group",
            required=False,
            )

    summary = Text(
            title=u"Summary",
            description=u"Summary of the group",
            required=False,
            )

    research_topic = TextLine(
            title=u"Research topic",
            description=u"Research topic name",
            required=False,
            )

    application_domain = TextLine(
            title=u"Application domain",
            description=u"Application domain the group focuses on",
            required=False,
            )

    team = Text(
            title=u"Team",
            description=u"People working in the group",
            required=False,
            )

    former_personell = Text(
            title=u"Former personell",
            description=u"People who used to work in the group",
            required=False,
            )

    group_details = Text(
            title=u"Group details",
            description=u"Detailed description of the group",
            required=False,
            )

    publications = Text(
            title=u"Publications",
            description=u"Publications related to the group",
            required=False,
            )
