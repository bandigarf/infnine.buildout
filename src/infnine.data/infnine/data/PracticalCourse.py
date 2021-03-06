from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class IPracticalCourse(Interface):
    """A practical course
    """

    title = TextLine(
            title=u"German Title",
            description=u"German title of the practical course",
            required=True,
            )

    title_english = TextLine(
            title=u"English Title",
            description=u"English title of the practical course",
            required=False,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the practical course",
            required=False,
            )

    practicalcourse_type = TextLine(
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

    practicalcourse_language = TextLine(
            title=u"Language",
            description=u"",
            required=False,
            )

    module = TextLine(
            title=u"Module",
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
            title=u"Body Info about Practical Course",
            description=u"Details, material, etc about the practical course",
            required=False,
            )
