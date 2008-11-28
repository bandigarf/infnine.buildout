from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class ISeminar(Interface):
    """A seminar
    """

    title = TextLine(
            title=u"English Title",
            description=u"English title of the seminar",
            required=True,
            )

    title_german = TextLine(
            title=u"German Title",
            description=u"German title of the seminar",
            required=False,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the seminar",
            required=False,
            )

    seminar_type = TextLine(
            title=u"Type",
            description=u"",
            required=False,
            )

    professor = TextLine(
            title=u"Professor",
            description=u"",
            required=False,
            )

    instructor = TextLine(
            title=u"Instructor",
            description=u"",
            required=False,
            )

    date_place = TextLine(
            title=u"Date, place",
            description=u"",
            required=False,
            )

    seminar_language = TextLine(
            title=u"Language",
            description=u"",
            required=False,
            )

    modul = TextLine(
            title=u"Modul",
            description=u"",
            required=False,
            )

    term = TextLine(
            title=u"Term",
            description=u"",
            required=False,
            )

    url = TextLine(
            title=u"URL",
            description=u"",
            required=False,
            )
    body = Text(
            title=u"Body Info about Seminar",
            description=u"Details, material, etc about the seminar",
            required=False,
            )
