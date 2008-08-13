from zope.component import createObject
from zope.formlib import form

from plone.app.form import base
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from collective.dtwidget import dtwidget

from Acquisition import aq_inner

from infnine.data.interfaces import IPerson
from infnine.data import _

class AddForm(base.AddForm):
    """Add form
    """

    form_fields = form.fields(IPerson)

    label = _(u"Add Person")
    form_name = _(u"Person Details")
    form_fields['alumni_date'].custom_widget = dtwidget
    form_fields['introduction'].custom_widget = WYSIWYGWidget
    form_fields['misc'].custom_widget = WYSIWYGWidget

    def setUpWidgets(self, ignore_request=False):
        self.widgets = form.setUpWidgets(
                self.form_fields,
                self.prefix,
                self.context,
                self.request,
                ignore_request=ignore_request,
                )

    def create(self, data):
        content = createObject(u"infnine.data.Person")
        form.applyChanges(content, self.form_fields, data)
        return content

class EditForm(base.EditForm):
    """Edit form
    """

    form_fields = form.fields(IPerson)

    label = _(u"Edit Person")
    form_name = _(u"Person Details")
    form_fields['alumni_date'].custom_widget = dtwidget
    form_fields['introduction'].custom_widget = WYSIWYGWidget
    form_fields['misc'].custom_widget = WYSIWYGWidget
