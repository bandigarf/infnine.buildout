from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class ITeachingListing(Interface):
    """The page for listing of teachings
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u"Teaching"
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
