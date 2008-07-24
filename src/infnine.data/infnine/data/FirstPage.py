from zope.interface import Interface
from zope import schema

from zope.app.container.constraints import contains

from infnine.data import ContentMessageFactory as _

class IFirstPage(Interface):
    """A First page
    """

    title = schema.TextLine(title=_(u"FirstPage title"),
                            required=True)
