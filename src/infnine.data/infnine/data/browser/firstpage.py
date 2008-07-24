"""Define a browser view for the Promotion content type. In the FTI 
configured in profiles/default/types/*.xml, this is being set as the default
view of that content type.
"""

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.memoize.instance import memoize
from Products.CMFCore.utils import getToolByName

class FirstPageView(BrowserView):
    """Default view of a promotion
    """

    __call__ = ViewPageTemplateFile('firstpage.pt')