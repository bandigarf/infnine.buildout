application_domains_list=(
    'Multi-Joint Action',
    'Intelligent Kitchen',
    'Cognitive Factory',
    'Soccer Analysis',
)

research_topics_list=(
    'Model-Based Image Interpretation',
    'Model Fitting',
    'Objective Functions, Learning Objective Functions',
    'Face Detection, Face Model Fitting, Head Tracking',
    'Facial Expression Recognition, Emotion Recognition',
    'Gaze Tracking, Focus of Interest',
    'Color Detection, Adaptive Skin Color Classification',
    'Person Localization, Person Tracking',

    'Knowledge Representation',
    'Learning Grounded Models',
    'Import of WWW Information Into the Knowledge Base',

    'Automatic Model Inference',
    'Descriptor Based 3D Localization',
    'Hybrid Approach 3D Localization',
    'Multimodal 3D Localization',
    'Object Tracking for Manipulation Tasks',
    'Hand Tracking in Combination With Object Localization',

    'Tracking Soccer Players',
    'Human Motion Capture, Tracking and Analysis',

    'Human Motions in Manipulation Tasks',
    'Human Motions as Model for Robot Controllers',

    'Constraint-Based Diagnosis and Planning',
    'Model-Based Reasoning',
    'Constraint Optimization Algorithms',
    'Model-Based Programming',
    'Probabilistic Reasoning',

    'Segmentation of Players in Broadcast Videos',
    'Statistical Relational Learning ',
    'Probabilistic Models',
    'Logical Models',
    'Graphical Models',
    'Parameter Learning',

    'Semantic Mapping',
    '3D Geometric Reasoning',
    'Probabilistic Model Fitting',

    'Automatic Planning',
    'Plan-Based Control',
    'Manufacturing',
    'Simulation',
    'RPL',

    'Automatic Analysis and Modeling of Sports Games',
    'Ontological Representation and Reasoning',
    'Data Mining / Knowledge Discovery',
    'Automated Learning',

    'Driver Assistant Systems',
    'Laser Segmentation',
    'Object Formation',
    'Environmental Perception',

    'Test Generation',
    'Model-Based Systems',
    'Real Time Systems',
    'Formal Specifications',
    'Temporal Logics',
    'Requirement Engineering',

    'Plan-Based Robot Control',
    'Plan Optimization',
    'Transformational Planning',
    'Multi-Robot Coordination',
    'Human and Robot Manipulation',
    'Motion Primitives',
    'Motor Control',

    'Cognition',
    'Intelligent Perception',
    'Plan-Based Control of Actions in Cognitive Factory',
    'Failure Diagnosis',
    'Ubiquitous Robotics',
    'Visual SLAM',
    'Applied Probabilistic Theory',
    'Object Models',
    'Action Language',
)

authors_list=(
    'bandouch',
    'beetz',
    'blodow',
    'buck',
    'dolha',
    'durus',
    'esden-tempski',
    'eggers',
    'fedrizzi',
    'gedikli',
    'haemmerle',
    'hanek',
    'hoyningen-huene',
    'jain',
    'kirchlechner',
    'kirsch',
    'klank',
    'kresse',
    'kruse',
    'kunze',
    'maldonado',
    'marton',
    'mayer',
    'moesenlechner',
    'mueller',
    'pangercic',
    'pietzsch',
    'radig',
    'riaz',
    'ruehr',
    'ruiz',
    'rusu',
    'schmitt',
    'schroeter',
    'siles',
    'stulp',
    'sun-li',
    'tenorth',
    'vazquez',
    'watanabe',
    'weikersdorfer',
    'wimmer',
)

professors = (
    'beetz',
    'radig',
)

project_types = (
    'Diploma Thesis',
    'Master Thesis',
    'Bachelor Thesis',
    'SEP',
    'IDP',
    'HiWi'
)

research_topics = [
    'Perception',
    'Models',
    'Representation',
    'Reasoning',
    'Learning',
    'Planning',
    'Action',
    'Human-Robot Interaction'
]

bib2html_groups_listing = [
    'FIPM',
    'EvI',
    'IU',
    'AGILO',
    'Cogmash',
    'Cop',
    'Memoman',
    'Cogman',
    'Mudis',
    'K4C',
    'Probcog',
    'Cogito',
    'Aspogamo',
    'Self-Diagnosis and Planning',
    'EnvMod',
    'Para',
    'Other'
    ]


bib2html_groups_mapping = {
    'K4C':'knowledge4cotesys',
    'FIPM':'aspogamo',
    'EvI':'',
    'IU':'face-mimic',
    'AGILO':'agilo',
    'Cogmash':'cogmash',
    'Cop':'cop',
    'Memoman':'memoman',
    'Cogman':'cogman',
    'Mudis':'mudis',
    'Probcog':'probcog',
    'Cogito':'cogito',
    'Aspogamo':'aspogamo',
    'Self-Diagnosis and Planning':'constraint-based-models-and-algorithms-for-self-diagnosis-and-planning',
    'EnvMod':'envmod',
    'Para':'para',
    'Other':''
}

#for sending notification emails upon thesis 
#announcement submition
#Affected Files:
#publishStudentProject.py
#content/studentproject.py

import os
host = os.popen('hostname').read().strip()
if host == 'www9':
    templateFile='/usr/local/share/infnine/theses/template.tex'
    destinationFile='/usr/local/share/infnine/theses/'
elif host == 'ias':
    templateFile='/usr/local/share/iasweb/theses/template.tex'
    destinationFile='/usr/local/share/iasweb/theses/'
elif host == 'lapradig94' or host == 'lapradig39':
    templateFile='/home/pangercic/programming/infnine.buildout/custom/templates/template.tex'
    destinationFile='/home/pangercic/programming/infnine.buildout/custom/templates'
else:
    print 'unknown hostname'

#toAddr='pangerci@in.tum.de'
toAddr='tenorth@in.tum.de'
fromAddr='webmaster@mail9.in.tum.de'

def filterNamesUrl(self,string):
    """Filter Names for {Umlaut} Strings and return corresponding ae, oe or ue -
    needed to create people's urls"""
    listUmlauts = ['{\\"a}', '{\\"o}', '{\\"u}', '\\"a', '\\"o', '\\"u']
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
    listUmlauts = ['{\\\\"a}', '{\\\\"o}', '{\\\\"u}', '\\\\"a', '\\\\"o', '\\\\"u', '{\\"a}', '{\\"o}', '{\\"u}', '\\"a', '\\"o', '\\"u']
    listVowels = {'a': u'\xe4', 'o': u'\xf6', 'u':u'\xfc'}
    for subStr in listUmlauts:
        if string.find(subStr) != -1:
            for vowel, umlaut  in listVowels.iteritems():
                if subStr.find(vowel) != -1:
                    return string.replace(subStr, umlaut)
    #No Umlaut found
    return string


def authors(self, string):
    """Processes the string coming from bibtex entry author field.
    If author with infnine chair it returns its url identifier, 
    if not it sorts umlauts and returns the full name - all together 
    in a list"""
    fullnameList = string.split(' and ')
    nameList = []
    nameInList = False
    for fullname in fullnameList:
        nameInList = False
        for name in fullname.split(' '):
            if filterNamesUrl(self, name) in authors_list:
                nameList.append(filterNamesUrl(self, name))
                nameInList = True
        if nameInList != True:
            nameList.append(filterNamesUmlaut(self, fullname))
    return nameList

def filtered_name(self, string = None):
    """Removes official titles from the person's name, e.g. Prof., Dr., ...)"""
    if string != None:
        if (type(string) == type("")) or (type(string) == type(u"")):
            ret = string
        else:
            ret = string.title
    else:
        ret = self.title
    ret = ret.replace("Prof.", "")
    ret = ret.replace("Dr.-Ing.", "")
    ret = ret.replace("Dr.", "")
    ret = ret.replace("Emeritus", "")
    ret = ret.replace("Ordinarius", "")
    ret = ret.replace("PhD", "")
    ret = ret.strip(" .,;")

    # swap surname & first name around (they are comma separated if reversed)
    l = ret.find(',')
    if l > 0:
        ret = ret[l+2:] + ' ' + ret[:l]

    ret = ret.strip()
    return ret

def reversePublicationList(self, list):
    sortedList = []
    while (list.__len__() > 0):
        sortedList.append(list.pop())

    return sortedList
