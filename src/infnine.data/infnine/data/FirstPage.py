from zope.interface import Interface
from zope.schema import TextLine, Text

class IFirstPage(Interface):
    """The first page
    """

    title = TextLine(
            title=u"First Page Title",
            description=u"Title of the first page",
            required=True,
            default=u"Index Page"
            )

    description = Text(
            title=u"Description",
            description=u"Description of the first page",
            required=False,
            )
