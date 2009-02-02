from zope.interface import Interface
from zope.schema import TextLine, Text

class ISemester(Interface):
    """The semester container
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u""
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
