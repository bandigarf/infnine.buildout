from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IStudentProject

class StudentProjectContent(Container):
    """Student Project Content
    """
    implements(IStudentProject,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Student Project"

    project_details = FieldProperty(IStudentProject['project_details'])

factory = Factory(
        StudentProjectContent,
        )
