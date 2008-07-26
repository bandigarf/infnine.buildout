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
            title=u"Summary",
            description=u"Summary of the research project",
            required=False,
            )

    # should be a list of objects of type IPerson
    # or, a text field with people aliases (approach #2)
    team = Text(
            title=u"Team",
            description=u"People working on the research project",
            required=False,
            )

    project_details = Text(
            title=u"Project details",
            description=u"Detailed description of the project",
            required=False,
            )

    # should be a list of objects of type IPublication
    # or, a text field with publication reference strings (approach #2)
    publications = Text(
            title=u"Publications",
            description=u"Publications related to the project",
            required=False,
            )

    # media is to be listed from media sub-folder
    # logo is to be a picture named logo
    # these will be listed/presented by the page template
