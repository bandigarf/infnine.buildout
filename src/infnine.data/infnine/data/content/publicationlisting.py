from plone.app.content.interfaces import INameFromTitle
from plone.app.content.item import Item
from plone.locking.interfaces import ITTWLockable

from zope.component.factory import Factory
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty

from infnine.data.interfaces import IPublicationListing

from infnine.data.common import authors_list

def filterNamesUrl(self, string):
    """Filter Names for {Umlaut} Strings and return corresponding ae, oe or ue - 
    needed to create people's urls"""
    listUmlauts = ['{\\\\"a}', '{\\\\"o}', '{\\\\"u}', '\\\\"a', '\\\\"o', '\\\\"u']
    listVowels = ['a', 'o', 'u']
    for subStr in listUmlauts:
        if string.find(subStr) != -1:
            for vowel  in listVowels:
                if subStr.find(vowel) != -1:
                    return string.replace(subStr, vowel+'e').lower()                    
    #No Umlaut found
    return string.lower()

def filterNamesUmlaut(self, string):
    """Filter Names for {Umlaut} Strings and return corresponding unicode umlauts - to 
    represent names of ppl without the Person page(title attribute)"""
    listUmlauts = ['{\\\\"a}', '{\\\\"o}', '{\\\\"u}', '\\\\"a', '\\\\"o', '\\\\"u']
    listVowels = {'a': u'\xe4', 'o': u'\xf6', 'u':u'\xfc', 'o':u'\xf6'}
    for subStr in listUmlauts:
        if string.find(subStr) != -1:
            for vowel, umlaut  in listVowels.iteritems():
                if subStr.find(vowel) != -1:
                    return string.replace(subStr, umlaut) 
    #No Umlaut found
    return string 

class PublicationListingContent(Item):
    """Page to list Chair Publications
    """
    implements(IPublicationListing,
            ITTWLockable,
            INameFromTitle)

    portal_type = "Publication Listing"
    author_list = authors_list
    fN = filterNamesUrl
    fNU = filterNamesUmlaut

factory = Factory(
        PublicationListingContent,
        )


