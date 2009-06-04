from zope.formlib import form

from infnine.data.interfaces import IContact, IContact2


class ContactAddForm(form.AddForm):
    """A simple add form for contacts."""

    form_fields = form.fields(IContact)

class ContactAddAnotherForm(form.AddForm):
    """A simple add form for contacts."""

    form_fields = form.fields(IContact2)





#     def setUpWidgets(self, ignore_request=False):
#         self.widgets = form.setUpWidgets(
#             self.form_fields,
#             self.prefix,
#             self.context,
#             self.request,
#             ignore_request=ignore_request,
#             )


#     def create(self, data):
#         content = createObject(u"infnine.data.Contact")
#         form.applyChanges(content, self.form_fields, data)
#         return content
