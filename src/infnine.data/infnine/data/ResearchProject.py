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

    # should be a list of objects of type IPerson
    staff = TextLine(
            title=u"Staff",
            description=u"People working on the research project",
            required=False,
            )
