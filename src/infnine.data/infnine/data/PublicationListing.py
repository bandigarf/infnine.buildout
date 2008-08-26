from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class IPublicationListing(Interface):
    """The page for listing of Chair Publications
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u"Publications"
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
