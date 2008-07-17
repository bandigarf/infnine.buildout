from zope.interface import Interface
from zope.schema import TextLine, URI, Int, Text, Choice

class IPerson(Interface):
    """A person
    """

    title = TextLine(
            title=u"Name",
            description=u"Display name of the person",
            required=True,
            )

    misc = Text(
            title=u"Misc",
            description=u"Miscellaneous",
            required=False,
            )
