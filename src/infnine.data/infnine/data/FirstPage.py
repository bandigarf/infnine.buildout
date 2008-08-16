from zope.interface import Interface
from zope.schema import TextLine, Text

class IFirstPage(Interface):
    """The first page
    """

    title = TextLine(
            title=u"FirstPage Title",
            description=u"Title of the first page",
            required=True,
            default=u"First Page"
            )

    description = Text(
            title=u"Description",
            description=u"Description of the first page",
            required=False,
            )
