from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class IPracticalCourse(Interface):
    """A practical course
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the practical course",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the practical course",
            required=False,
            )
