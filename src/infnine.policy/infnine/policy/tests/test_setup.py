import unittest
from Products.CMFCore.utils import getToolByName
from infnine.policy.tests.base import InfninePolicyTestCase

class TestSetup(InfninePolicyTestCase):
    def afterSetUp(self):
        self.workflow = getToolByName(self.portal, 'portal_workflow')
        self.acl_users = getToolByName(self.portal, 'acl_users')
        self.types = getToolByName(self.portal, 'portal_types')

    def test_portal_title(self):
        self.assertEquals("Infnine Portal",
                           self.portal.getProperty('title'))

    def test_portal_description(self):
        self.assertEquals("Welcome to Infnine Portal",
                           self.portal.getProperty('description'))

    def test_role_aded(self):
        self.failUnless("Student",
                         self.portal.validRoles())

    def test_view_permission_for_student(self):
        self.failUnless('View' in [r['name'] for r in
        self.portal.permissionsOfRole('Reader') if r['selected']])
        self.failUnless('View' in [r['name'] for r in
        self.portal.permissionsOfRole('Student') if r['selected']])

    def test_student_group_added(self):
        self.assertEquals(1, len(self.acl_users.searchGroups(name='Students')))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
