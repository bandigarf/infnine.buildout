#run from buildout like:
#./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope
from infnine.data.readdb import getEvents
semester = semester_id = 'SS2010'
semester = getEvents(semester_id)

def flatten(x):
    result = []
    for el in x:
        #if isinstance(el, (list, tuple)):
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def flatlist2string(l):
    s = u''
    for el in l:
        s += el.decode('utf-8')
        if not el is l[len(l)-1]:
            s += ', '
    return s

def num2str2(num):
    if num >= 0:
        if num < 10:
            return '0' + `num`
        elif num < 100:
            return `num`
        else:
            return `num`[-2:]

def datelist2string(datelist):
    if len(datelist) == 0:
        return u''
    s = u''
    for dateitem in datelist:
        if len(dateitem) != 0:
            s += dateitem['Day'] + ', ' \
               + `dateitem['StartHour']` + ':' + num2str2(dateitem['StartMinute']) + '-' \
               + `dateitem['EndHour']` + ':' + num2str2(dateitem['EndMinute']) + ', ' \
               + dateitem['Room'] \
               + ', '
    return s[:-2]

def keymap(event_type, key):
    keymap_generic = {
        'English Title': 'title_english',
        'German Title': 'title',
        #description
        #details
        'Professor': 'professor',
        'Instructor': 'instructor',
        'Date': 'date_place',
        'Module': 'module',
        #term
        'Url': 'url',
    }

    if key in keymap_generic.keys():
        return keymap_generic[key]

    if key in ('Type', 'Language'):
        return event_type + '_' + key.lower()

    print "!!! Don't know how to handle key:", key
    return None

def setvalue(zodb_object, key, value):
    eventtype_prefix = {
        'Lecture': 'lecture',
        'Practical Course': 'practicalcourse',
        'Seminar': 'seminar'
    }
    zodb_key = keymap(eventtype_prefix[zodb_object.meta_type], key)
    if zodb_key:
        if key == 'Language':
            zodb_object.__setattr__(zodb_key, [u'German', u'English'][value])
        elif key in ('Professor', 'Instructor'):
            zodb_object.__setattr__(zodb_key, flatlist2string(flatten(value)))
        elif key == 'Module':
            zodb_object.__setattr__(zodb_key, str(value[1]).decode('utf-8'))
        elif key == 'Date':
            zodb_object.__setattr__(zodb_key, datelist2string(value))
        else:
            zodb_object.__setattr__(zodb_key, str(value).decode('utf-8'))
    else:
        pass

if ('app' in dir()) and (app != None):
    print "Running in Zope, creating objects in ZODB..."
    teaching = app.infnine.teaching

if not teaching.hasObject(semester_id.lower()):
    print "Semester", semester_id, "not yet in ZODB, creating"
    admin = app.acl_users.getUser('admin')
    import AccessControl
    AccessControl.SecurityManagement.newSecurityManager(None, admin)
    from Testing.makerequest import makerequest
    app = makerequest(app)

    teaching.invokeFactory('Semester', semester_id.lower())

    sem = teaching.__getitem__(semester_id.lower())
    sem.title = semester_id
    sem.reindexObject()
    import transaction
    transaction.commit()

if not 'sem' in dir():
    sem = teaching.__getitem__(semester_id.lower())

for id in semester.keys():
    event = semester[id]
    t = semester[id]['Type']
    if (t == 'Wahlpflichtvorlesung') or (t == 'Vertiefungsvorlesung'):
        event_type = 'Lecture'
    elif (t == 'Praktikum') or (t == 'Master-Praktikum'):
        event_type = 'Practical Course'
    else:
        event_type = 'Seminar'

    if not sem.hasObject(`id`):
        print "Entry", `id`, "not yet in ZODB, creating"
        admin = app.acl_users.getUser('admin')
        import AccessControl
        AccessControl.SecurityManagement.newSecurityManager(None, admin)
        from Testing.makerequest import makerequest
        app = makerequest(app)

        sem.invokeFactory(event_type, `id`)

    event_zodb = sem.__getitem__(`id`)

    keys = event.keys()
    print "Updating", `id`, keys
    for key in keys:
        setvalue(event_zodb, key, event[key])

    event_zodb.reindexObject()
    import transaction
    transaction.commit()
