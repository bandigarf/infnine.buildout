from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Datetime, Bool

from infnine.data.common import research_topics_list

class IPerson(Interface):
    """A person
    """

    title = TextLine(
            title=u"Name",
            description=u"Display name of the person",
            required=True,
            )

    status = Choice(
            title=u"Status",
            description=u"Status of the person",
            required=True,
            default="Other",
            values=("Professor", "Guest Lecturer",  "Junior Research Group Leader", "Secretariat", "Researcher",
                    "Visiting Researcher", "Alumnus", "Administration", "Student Member",
                    "External", "Other",
                    ),
            )

    alumni_date = Datetime(
            title=u"Alumni Date",
            description=u"The date when the person has become an alumnus",
            required=False,
            )

    position = TextLine(
            title=u"Position",
            description=u"Position of the person at the chair",
            required=False,
            )

    department = TextLine(
            title=u"Department",
            description=u"Department of the person",
            required=False,
            )

    email = TextLine(
            title=u"E-Mail",
            description=u"Electronic mail address",
            required=False,
            )

    telephone = TextLine(
            title=u"Telephone FMI",
            description=u"Telephone number at FMI",
            required=False,
            )
    telephone1 = TextLine(
        title=u"Telephone CCRL II",
        description=u"Telephone number at CCRL II",
        required=False,
        )

    fax = TextLine(
            title=u"Fax",
            description=u"Fax number",
            required=False,
            )

    office = TextLine(
            title=u"Office FMI",
            description=u"Office number at FMI",
            required=False,
            )

    office1 = TextLine(
        title=u"Office CCRL II",
        description=u"Office number at CCRL II",
        required=False,
        )

    introduction = Text(
            title=u"Introduction",
            description=u"Introduction",
            required=False,
            )

    research_topics = List(
            title=u"Research Topics",
            description=u"",
            required=False,
            unique=True,
            value_type=Choice(
                    title=u"Research Topic",
                    values=research_topics_list,
                    ),
            )

    research_projects_current = Text(
            title=u"Current research projects",
            description=u"Research projects the person is currently active in, enter line by line url part name of project",
            required=False,
            )

    research_projects_former = Text(
            title=u"Former research projects",
            description=u"Research projects the person was active in, enter line by line url part name of project",
            required=False,
            )

    teaching = Text(
            title=u"Teaching",
            description=u"Teaching events, enter line by line url part name of the teaching event(int number)",
            required=False,
            )
    teaching_misc = Text(
            title=u"Teaching Misc",
            description=u"Put courses as html that are not held by Inf9",
            required=False,
            )

    students = Text(
            title=u"Students",
            description=u"Line by line url part name of the students working for you, must have page at the chair",
            required=False,
            )

    misc = Text(
            title=u"Misc",
            description=u"Miscellaneous",
            required=False,
            )

    publications = Text(
            title=u"Publications",
            description=u"Only selected Publications, enter line by line bibtex citation string",
            required=False,
            )
    show_link_all_publications = Bool(
            title=u"linkToPublications",
            description=u"Toggle this to display link to all your publications",
            default=False,
            )
    show_link_teaching = Bool(
            title=u"linkTeaching",
            description=u"Toggle this to display link to all your lectures",
            default=False,
            )
