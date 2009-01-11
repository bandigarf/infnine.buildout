from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IStudentProject

#from infnine.data.publishStudentProject import *

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
    publish_to_drehscheibe = FieldProperty(IStudentProject['publish_to_drehscheibe'])

factory = Factory(
        StudentProjectContent,
        )

def publishStudentProject(obj, event):
    print "bla"
#    if not obj.publish_to_drehscheibe:
#        if obj._published:
            # do something to unpublish it
            #obj._published = False
#        return

    #import pdb;pdb.set_trace()
#    if obj._published:
        # do something to update it
#        return

    # publish object
#    print "publish_to_drehscheibe:", obj.publish_to_drehscheibe
#    obj._published = True

    #obj.reindexObject()
