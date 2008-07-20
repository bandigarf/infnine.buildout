import unittest
from infnine.policy.tests.base import InfninePolicyTestCase

class TestSetup(InfninePolicyTestCase):
    def test_portal_title(self):
        self.assertEquals("Infnine Portal", self.portal.getProperty('title'))

    def test_portal_description(self):
        self.assertEquals("Welcome to Infnine Portal",
                           self.portal.getProperty('description'))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
