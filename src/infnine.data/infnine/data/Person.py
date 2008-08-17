from zope.interface import Interface
from zope.schema import TextLine, Text, List, Choice, Datetime

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
            values=("Professor", "Junior Research Group Leader", "Secretariat", "Researcher",
                    "Visiting Researcher", "Alumnus", "Administration", "Student Member", "External", "Other"),
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

    introduction = Text(
            title=u"Introduction",
            description=u"Introduction",
            required=False,
            )

    publications = Text(
            title=u"Publications",
            description=u"",
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
                    )
            )

    research_projects_current = Text(
            title=u"Current research projects",
            description=u"Research projects the person is currently active in",
            required=False,
            )

    research_projects_former = Text(
            title=u"Former research projects",
            description=u"Research projects the person was active in",
            required=False,
            )

    teaching = Text(
            title=u"Teaching",
            description=u"",
            required=False,
            )

    students = Text(
            title=u"Students",
            description=u"",
            required=False,
            )

    misc = Text(
            title=u"Misc",
            description=u"Miscellaneous",
            required=False,
            )
