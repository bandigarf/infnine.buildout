from zope.interface import Interface
from zope.schema import TextLine, Text

class IPeoplePage(Interface):
    """The page for listing people
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u"People"
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
