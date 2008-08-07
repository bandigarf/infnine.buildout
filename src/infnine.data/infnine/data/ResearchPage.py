from zope.interface import Interface
from zope.schema import TextLine, Text

class IResearchPage(Interface):
    """The page for listing research projects
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u"Research"
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
