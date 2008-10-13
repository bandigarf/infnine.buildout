from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int

class IStudentProject(Interface):
    """A student project
    """

    title = TextLine(
            title=u"Title",
            description=u"Title of the student project",
            required=True,
            )

    description = Text(
            title=u"Description",
            description=u"A short description of the student project",
            required=False,
            )

    project_details = Text(
            title=u"Project details",
            description=u"Detailed description of the project",
            required=False,
            )
