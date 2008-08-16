from zope.component import createObject
from zope.formlib import form

from plone.app.form import base
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget

from Acquisition import aq_inner

from infnine.data.interfaces import IGroup
from infnine.data import _

class AddForm(base.AddForm):
    """Add form
    """

    form_fields = form.fields(IGroup)

    label = _(u"Add Group")
    form_name = _(u"Group Details")
    form_fields['group_details'].custom_widget = WYSIWYGWidget

    def setUpWidgets(self, ignore_request=False):
        self.widgets = form.setUpWidgets(
                self.form_fields,
                self.prefix,
                self.context,
                self.request,
                ignore_request=ignore_request,
                )

    def create(self, data):
        content = createObject(u"infnine.data.Group")
        form.applyChanges(content, self.form_fields, data)
        return content

class EditForm(base.EditForm):
    """Edit form
    """

    form_fields = form.fields(IGroup)

    label = _(u"Edit Group")
    form_name = _(u"Group Details")
    form_fields['group_details'].custom_widget = WYSIWYGWidget
