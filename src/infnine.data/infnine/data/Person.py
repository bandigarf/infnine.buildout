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

    position = TextLine(
            title=u"Position",
            description=u"Position of the person at the chair",
            required=False,
            )

    email = TextLine(
            title=u"E-Mail",
            description=u"Electronic mail address",
            required=False,
            )

    telephone = TextLine(
            title=u"Telephone",
            description=u"Telephone number",
            required=False,
            )

    fax = TextLine(
            title=u"Fax",
            description=u"Fax number",
            required=False,
            )
    office = TextLine(
            title=u"Office",
            description=u"Office number",
            required=False,
            )

    misc = Text(
            title=u"Misc",
            description=u"Miscellaneous",
            required=False,
            )
