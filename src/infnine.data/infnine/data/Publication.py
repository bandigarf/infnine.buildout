from zope.interface import Interface
from zope.schema import TextLine, Text, Choice, Int

class IPublication(Interface):
    """A publication
    """

    pubtype = Choice(
            title=u"Type",
            description=u"Type of publication",
            required=False,
            values = ('InProcedings', 'Article', 'PhdThesis')
            )

    title = TextLine(
            title=u"Title",
            description=u"Title of the publication",
            required=True,
            )

    # should be a list of objects of type IPerson
    author = TextLine(
            title=u"Author(s)",
            description=u"Author(s) of the publication",
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

    bib2html_groups = TextLine(
            required=False,
            )

    bib2html_pubtype = TextLine(
            required=False,
            )

    bib2html_rescat = TextLine(
            required=False,
            )

    bib2html_funding = TextLine(
            required=False,
            )
