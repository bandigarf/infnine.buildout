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
    journal = FieldProperty(IPublication['journal'])
    booktitle = FieldProperty(IPublication['booktitle'])
    year = FieldProperty(IPublication['year'])
    note = FieldProperty(IPublication['note'])
    abstract = FieldProperty(IPublication['abstract'])
    bib2html_groups = FieldProperty(IPublication['bib2html_groups'])
    bib2html_pubtype = FieldProperty(IPublication['bib2html_pubtype'])
    bib2html_rescat = FieldProperty(IPublication['bib2html_rescat'])
    bib2html_funding = FieldProperty(IPublication['bib2html_funding'])

factory = Factory(
        PublicationContent,
        )
