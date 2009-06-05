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

    bib2html_funding = Text(
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

    bib2html_groups = TextLine(
            title=u"Groups",
            description=u"Groups, internal or external",
            required=False,
            )

    bib2html_rescat = TextLine(
            title=u"Rescat",
            description=u"",
            required=False,
            )

    publisher = TextLine(
            title=u"Publisher",
            description=u"",
            required=False,
            )

    issn = TextLine(
            title=u"ISSN",
            description=u"",
            required=False,
            )

    isbn = TextLine(
            title=u"ISBN",
            description=u"",
            required=False,
            )

    address = TextLine(
            title=u"Address",
            description=u"",
            required=False,
            )

    volume = TextLine(
            title=u"Volume",
            description=u"",
            required=False,
            )

    doi = TextLine(
            title=u"DOI",
            description=u"",
            required=False,
            )

    pages = TextLine(
            title=u"Pages",
            description=u"",
            required=False,
            )

    number = TextLine(
            title=u"Number",
            description=u"",
            required=False,
            )

    url = TextLine(
            title=u"URL",
            description=u"",
            required=False,
            )

    howpublished = TextLine(
            title=u"Howpublished",
            description=u"",
            required=False,
            )

    keywords = TextLine(
            title=u"Keywords",
            description=u"",
            required=False,
            )

    priority = TextLine(
            title=u"Priority",
            description=u"",
            required=False,
            )

    month = TextLine(
            title=u"Month",
            description=u"",
            required=False,
            )

    bib2html_pubtype = TextLine(
            title=u"bib2html_pubtype",
            description=u"",
            required=False,
            )

    bib2html_keywords = TextLine(
            title=u"bib2html_keywords",
            description=u"",
            required=False,
            )

    school = TextLine(
            title=u"School",
            description=u"",
            required=False,
            )

    pdf = TextLine(
            title=u"Pdf",
            description=u"",
            required=False,
            )

    citeulike_article_id = TextLine(
            title=u"citeulike-article-id",
            description=u"",
            required=False,
            )

    bibtex_entry = Text(
            title=u"BibTeX entry",
            description=u"BibTex entry of the publication",
            required=False,
            )

    bib2html_domain = TextLine(
        title=u"bib2html_domain",
        description=u"Research Domain",
        required=False,
        )

    institution = TextLine(
        title=u"institution",
        description=u"Institution",
        required=False,
        )

    organization = TextLine(
        title=u"organization",
        description=u"Organization",
        required=False,
        )

    editor = TextLine(
        title=u"editor",
        description=u"Editor",
        required=False,
        )

    series = TextLine(
        title=u"series",
        description=u"Series",
        required=False,
        )
