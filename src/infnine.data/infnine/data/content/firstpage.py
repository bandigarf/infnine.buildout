"""Definition of the FirstPage content type. See cinemafolder.py for more
explanation on the statements below.
"""

from zope.interface import implements
from zope.component import adapts

from Products.Archetypes import atapi
from Products.validation import V_REQUIRED

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from infnine.data.interfaces import IFirstPage
from infnine.data.config import PROJECTNAME

from infnine.data import ContentMessageFactory as _

FirstPageSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    ))

FirstPageSchema['title'].storage = atapi.AnnotationStorage()
FirstPageSchema['title'].widget.label = _(u"FirstPage title")
FirstPageSchema['title'].widget.description = _(u"")

FirstPageSchema['description'].storage = atapi.AnnotationStorage()
FirstPageSchema['description'].widget.label = _("Short description")
FirstPageSchema['description'].widget.description = _(u"")

finalizeATCTSchema(FirstPageSchema, folderish=False, moveDiscussion=False)

class FirstPage(base.ATCTContent):
    """Describe a FirstPage.
    """
    implements(IFirstPage)

    portal_type = "FirstPage"
    _at_rename_after_creation = True
    schema = FirstPageSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(FirstPage, PROJECTNAME)