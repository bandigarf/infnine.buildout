from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Int, Datetime, Bool

from infnine.data.common import project_types, professors, authors_list

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

    project_type = List(
            title=u"Type",
            description=u"Project type",
            required=False,
            unique=True,
            value_type=Choice(
                title=u"Type",
                values=project_types,
                ),
            )

    project_overview = Text(
            title=u"Project overview",
            description=u"Background info about the project",
            required=False,
            )

    task_description = Text(
            title=u"Task Description",
            description=u"What is expected during the project?",
            required=False,
            )

    prerequisites = Text(
            title=u"Prerequisites",
            description=u"A list of prerequisites",
            required=False,
            )

    professor = Choice(
            title=u"Professor",
            description=u"Professor",
            required=False,
            values=professors,
            )

    supervisor = Choice(
            title=u"Supervisor",
            description=u"Project supervisor",
            required=False,
            values=authors_list,
            )

    state = Choice(
            title=u"State",
            description=u"Project state",
            required=False,
            values=('Open', 'Running', 'Completed'),
            )

    student = TextLine(
            title=u"Student",
            description=u"Student name",
            required=False,
            )

    start_date = Datetime(
            title=u"Start Date",
            description=u"Start date of the project",
            required=False,
            )

    end_date = Datetime(
            title=u"End Date",
            description=u"End date of the project",
            required=False,
            )

    publish_to_drehscheibe = Bool(
            title=u"publishToDresheibe Selector",
            default=False,
            )
