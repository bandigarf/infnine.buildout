from zope.interface import Interface
from zope.schema import TextLine, Text

class IApplicationDomain(Interface):
    """An Application Domain
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the application domain",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the application domain",
            required=False,
            )

    details = Text(
            title=u"Details",
            description=u"A long description of the application domain",
            required=False,
            )
