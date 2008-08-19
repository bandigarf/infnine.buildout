from zope.interface import Interface
from zope.schema import TextLine, Text, Choice, Int

class IPublication(Interface):
    """A publication
    """

    pubtype = TextLine(
            title=u"Type",
            description=u"Type of publication",
            required=False,
            )

    title = TextLine(
            title=u"Title",
            description=u"Title of the publication",
            required=True,
            )

    author = Text(
            title=u"Author(s)",
            description=u"Author(s) of the publication",
            required=False,
            )

    funded_by = Text(
            title=u"Funded by",
            description=u"The party that provided funding for the publication",
            required=False,
            )

    journal = TextLine(
            title=u"Journal",
            description=u"Journal in which it was published",
            required=False,
            )

    booktitle = TextLine(
            title=u"Book",
            description=u"Book in which it was published",
            required=False,
            )

    year = Int(
            title=u"Year",
            description=u"Year of publication",
            required=False,
            )

    note = TextLine(
            title=u"Note",
            description=u"Additional note",
            required=False,
            )

    abstract = Text(
            title=u"Abstract",
            description=u"Short abstract of the publication",
            required=False,
            )

    groups = TextLine(
            title=u"Groups",
            description=u"Groups, internal or external",
            required=False,
            )

    rescat = TextLine(
            title=u"Rescat",
            description=u"",
            required=False,
            )

    bibtex_entry = Text(
            title=u"BibTeX entry",
            description=u"BibTex entry of the publication",
            required=False,
            )
