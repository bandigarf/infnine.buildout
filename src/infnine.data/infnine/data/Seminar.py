from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class ISeminar(Interface):
    """A seminar
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the seminar",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the seminar",
            required=False,
            )
