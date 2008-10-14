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

    project_type = FieldProperty(IStudentProject['project_type'])
    project_overview = FieldProperty(IStudentProject['project_overview'])
    task_description = FieldProperty(IStudentProject['task_description'])
    prerequisites = FieldProperty(IStudentProject['prerequisites'])
    professor = FieldProperty(IStudentProject['professor'])
    supervisor = FieldProperty(IStudentProject['supervisor'])
    state = FieldProperty(IStudentProject['state'])
    student = FieldProperty(IStudentProject['student'])
    start_date = FieldProperty(IStudentProject['start_date'])
    end_date = FieldProperty(IStudentProject['end_date'])

factory = Factory(
        StudentProjectContent,
        )
