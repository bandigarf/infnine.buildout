from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class ILecture(Interface):
    """A lecture
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the lecture",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the lecture",
            required=False,
            )
