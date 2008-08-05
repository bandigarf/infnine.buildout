from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPublication

class PublicationContent(Container):
    """Publication Content
    """
    implements(IPublication,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Publication"

    pubtype = FieldProperty(IPublication['pubtype'])
    author = FieldProperty(IPublication['author'])
    funded_by = FieldProperty(IPublication['funded_by'])
    journal = FieldProperty(IPublication['journal'])
    booktitle = FieldProperty(IPublication['booktitle'])
    year = FieldProperty(IPublication['year'])
    note = FieldProperty(IPublication['note'])
    abstract = FieldProperty(IPublication['abstract'])
    groups = FieldProperty(IPublication['groups'])
    rescat = FieldProperty(IPublication['rescat'])
    bibtex_entry = FieldProperty(IPublication['bibtex_entry'])

factory = Factory(
        PublicationContent,
        )
