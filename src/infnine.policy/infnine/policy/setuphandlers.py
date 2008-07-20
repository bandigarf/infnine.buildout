from Products.CMFCore.utils import getToolByName
def setupGroups(portal):
    acl_users = getToolByName(portal, 'acl_users')
    if not acl_users.searchGroups(name='Students'):
        gtool = getToolByName(portal, 'portal_groups')
        gtool.addGroup('Students', roles=['Student'])
def importVarious(context):
    """Miscellanous steps import handle
    """
    if context.readDataFile('infnine.policy_various.txt') is None:
        return
    portal = context.getSite()
    setupGroups(portal)
