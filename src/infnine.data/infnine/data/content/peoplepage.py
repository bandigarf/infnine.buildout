from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPeoplePage

from DocumentTemplate import sequence

def sortPeople(self, peopleListUnsorted):
    peopleListSorted = []
    peopleListSorted = sequence.sort(peopleListUnsorted, (('id', 'nocase', 'asc'),))    
    return peopleListSorted
    

class PeoplePageContent(Item):
    """Page to list people
    """
    implements(IPeoplePage,
            ITTWLockable,
            INameFromTitle)

    portal_type = "People Page"
    pLS = sortPeople

factory = Factory(
        PeoplePageContent,
        )


