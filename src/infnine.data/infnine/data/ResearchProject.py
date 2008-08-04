from zope.interface import Interface
from zope.schema import TextLine, Text, Choice, Int

class IResearchProject(Interface):
    """A research project
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the research project",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the research project",
            required=False,
            )

    summary = Text(
            title=u"Summary",
            description=u"Summary of the research project",
            required=False,
            )

    research_topic = TextLine(
            title=u"Research topic",
            description=u"Research topic name",
            required=False,
            )

    application_domain = TextLine(
            title=u"Application domain",
            description=u"Application domain of the project",
            required=False,
            )

    team = Text(
            title=u"Team",
            description=u"People working on the research project",
            required=False,
            )

    former_personell = Text(
            title=u"Former personell",
            description=u"People who used to work on the project",
            required=False,
            )

    project_details = Text(
            title=u"Project details",
            description=u"Detailed description of the project",
            required=False,
            )

    publications = Text(
            title=u"Publications",
            description=u"Publications related to the project",
            required=False,
            )

    # media is to be listed from media sub-folder
    # logo is to be a picture named logo
    # these will be listed/presented by the page template
