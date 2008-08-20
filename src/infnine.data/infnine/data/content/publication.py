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
    bib2html_funding = FieldProperty(IPublication['bib2html_funding'])
    journal = FieldProperty(IPublication['journal'])
    booktitle = FieldProperty(IPublication['booktitle'])
    year = FieldProperty(IPublication['year'])
    note = FieldProperty(IPublication['note'])
    abstract = FieldProperty(IPublication['abstract'])
    bib2html_groups = FieldProperty(IPublication['bib2html_groups'])
    bib2html_rescat = FieldProperty(IPublication['bib2html_rescat'])
    issn = FieldProperty(IPublication['issn'])
    isbn = FieldProperty(IPublication['isbn'])
    number = FieldProperty(IPublication['number'])
    month = FieldProperty(IPublication['month'])
    keywords = FieldProperty(IPublication['keywords'])
    priority = FieldProperty(IPublication['priority'])
    bib2html_pubtype = FieldProperty(IPublication['bib2html_pubtype'])
    bib2html_keywords = FieldProperty(IPublication['bib2html_keywords'])
    howpublished = FieldProperty(IPublication['howpublished'])
    citeulike_article_id = FieldProperty(IPublication['citeulike_article_id'])
    volume = FieldProperty(IPublication['volume'])
    address = FieldProperty(IPublication['address'])
    pages = FieldProperty(IPublication['pages'])
    publisher = FieldProperty(IPublication['publisher'])
    school = FieldProperty(IPublication['school'])
    doi = FieldProperty(IPublication['doi'])
    url = FieldProperty(IPublication['url'])
    pdf = FieldProperty(IPublication['pdf'])
    bibtex_entry = FieldProperty(IPublication['bibtex_entry'])

factory = Factory(
        PublicationContent,
        )
