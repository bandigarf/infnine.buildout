import zope.interface
import zope.schema

class IContact(zope.interface.Interface):
    """A simple contact."""

    firstName = zope.schema.TextLine(
        title=u"First Name",
        required=True)

    lastName = zope.schema.TextLine(
        title=u"Last Name",
        required=True)

class IContact2(zope.interface.Interface):
    """A simple contact."""

    firstName = zope.schema.TextLine(
        title=u"First Name",
        required=True)

    lastName = zope.schema.TextLine(
        title=u"Last Name",
        required=True)
