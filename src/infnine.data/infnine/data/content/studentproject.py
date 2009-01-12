from plone.app.content.interfaces import INameFromTitle
from plone.app.content.container import Container
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IStudentProject

from infnine.data.publishStudentProject import *

#needed for portal object
from zope.component import getSiteManager
#needed for mailhost object
from Products.CMFCore.utils import getToolByName

#some defines, change in common.py
from infnine.data.common import toAddr, fromAddr, destinationFile

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
  #needed to get portal object
  portalRoot = getSiteManager();
  if obj.publish_to_drehscheibe:
     publishStudentProject1(obj.project_type, portalRoot.people.__getitem__(obj.supervisor.title().lower()).title,\
     portalRoot.people.__getitem__(obj.professor.title().lower()).title,\
     portalRoot.people.__getitem__(obj.supervisor.title().lower()).email, obj.title, obj.project_overview,  \
     obj.task_description, obj.prerequisites,\
     #for some reason, absolute_url() returns '/infnine' doubled 
     portalRoot.absolute_url().replace('/infnine', '', 1)+ '/teaching/student-projects/' + obj.title.replace(' ', '-')\
     .lower())
     #context = aq_inner()
     mailhost = getToolByName(portalRoot, 'MailHost')
     author = portalRoot.people.__getitem__(obj.supervisor.title().lower()).title
     title = obj.title.replace(' ', '-').lower()
     mMsg = """New thesis Announcement by %s placed in: %s%s.tex"""
     message = mMsg % (author,destinationFile,title)
     mailhost.send(utf8a(message), toAddr, fromAddr, 'New Thesis Announcement')

#TODO:
#What will happen if one wants to amend an already submitted thesis proposal?
#For now let it just get overwritten
