from zope.interface import Interface
from zope.schema import TextLine, Text

class IAlumniPage(Interface):
    """The page for listing alumni
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u"Alumni"
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
