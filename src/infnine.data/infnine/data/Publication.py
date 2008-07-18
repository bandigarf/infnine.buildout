from zope.interface import Interface
from zope.schema import TextLine, Text

class IPublication(Interface):
    """A publication
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the publication",
            required=True,
            )
