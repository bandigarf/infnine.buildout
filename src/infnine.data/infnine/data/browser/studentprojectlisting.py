from zope.component import createObject
from zope.formlib import form

from plone.app.form import base

from Acquisition import aq_inner

from infnine.data.interfaces import IStudentProjectListing
from infnine.data import _

class AddForm(base.AddForm):
    """Add form
    """

    form_fields = form.fields(IStudentProjectListing)

    label = _(u"Add Student Project Listing Page")
    form_name = _(u"Student Project Listing Details")

    def setUpWidgets(self, ignore_request=False):
        self.widgets = form.setUpWidgets(
                self.form_fields,
                self.prefix,
                self.context,
                self.request,
                ignore_request=ignore_request,
                )

    def create(self, data):
        content = createObject(u"infnine.data.StudentProjectListing")
        form.applyChanges(content, self.form_fields, data)
        return content

class EditForm(base.EditForm):
    """Edit form
    """

    form_fields = form.fields(IStudentProjectListing)

    label = _(u"Add Student Project Listing Page")
    form_name = _(u"Student Project Listing Details")
