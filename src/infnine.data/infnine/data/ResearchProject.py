from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

from infnine.data.common import research_topics_list
from infnine.data.common import application_domains_list

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

    research_topics = List(
            title=u"Research Topics",
            description=u"Research topics covered by the project",
            required=False,
            unique=True,
            value_type=Choice(
                    title=u"Research Topic",
                    values=research_topics_list,
                    ),
            )

    application_domain = List(
            title=u"Application domain",
            description=u"Application domain of the project",
            required=False,
            unique=True,
            value_type=Choice(
                    title=u"Application Domain",
                    values=application_domains_list,
                    ),
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
