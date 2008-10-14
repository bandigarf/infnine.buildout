from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class IStudentProjectListing(Interface):
    """The page for listing of student projects
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the page",
            required=True,
            default=u"Student Projects"
            )

    description = Text(
            title=u"Description",
            description=u"Description",
            required=False,
            )
