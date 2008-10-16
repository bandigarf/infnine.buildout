#The script returns a dict with unique IDs of events(lectures, etc) from the database.
#To be displayed are following fields (in order as they appear here):
#English Title
#German Title
#Professor
#Instructor
#Type
#Language
#Date
#Module
#Url

#set printDict = True if you want pretty print
#pass WSYYYY or SSYYYY to getEvents function to get the desired semester

#CLASSIFICATION:
#TYPE
#   if Type == Wahlpflichtvorlesung OR Vertiefungsvorlesung:
#       Lecture
#   elif Type == Praktikum:
#        Practical Course
#   else:
#        Seminar

#LANGUAGE
#    if Language == 1"
#        English
#    else:
#        German

     
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55Applet begins here
import MySQLdb

def getEvents(sem):
    #connect to DB oberseminar
    db = MySQLdb.connect(   host="sqlradig.informatik.tu-muenchen.de", user="dejan", passwd="infninetest", db="oberseminar")
    cursor = db.cursor()
    #query ID, ETitelVoll, DTitelVoll, Typ, englisch, url, ID is a unique id in lv_findet_statt_ex DB
    cursor.execute ("""SELECT ID, ETitelVoll, DTitelVoll, Typ, englisch, url FROM `lv_findet_statt_ex` WHERE Semester=%s""", (sem,))
    rows = cursor.fetchall()
    #dict for all events
    events = {}
    #dict for first query
    event = {}
    #who is holding lecture
    professor = []
    #who is tutoring lecture
    instructor = []
    #when it takes place
    date = []
    #what is it's faculty's unique ID
    module = [] 
    #loop
    for row in rows:
        #print  "ID: ", row[0], "\nEnglishTitle: ", row[1], "\nGermanTitle: ", row[2], "\nType: ", row[3] 
        event['English Title'] = row[1]
        event['German Title'] = row[2]
        event['Type'] = row[3]
        event['Language'] = row[4]
        event['Url'] = row[5]
        events[int(row[0])] = event
        professor.append(int(row[0]))
        instructor.append(int(row[0]))
        date.append(int(row[0]))
        module.append(int(row[0]))
        event = {}

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#find profs holding lecture
    for idkey in professor:
        cursor.execute ("""SELECT name FROM person p JOIN lv_leiter l ON p.id=l.PID WHERE l.FSID=%s""", (idkey,))   
        rows = cursor.fetchall()
        event_tmp = events[idkey]
        event_tmp['Professor'] = rows
        events[idkey] = event_tmp

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#find instructors tutoring lecture
    for idkey in instructor:
        cursor.execute ("""select name from person p join lv_betreuer b on p.id=b.PID where b.FSID=%s""", (idkey,))   
        rows = cursor.fetchall()
        event_tmp = events[idkey]
        event_tmp['Instructor'] = rows
        events[idkey] = event_tmp
      
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#find time, room, type of appointment lecture      
    li = []
    dateElem = {}
    for idkey in date:
        cursor.execute ("""select startHour, startMinute, endHour, endMinute, startDate, endDate,
        room, wochentag, terminart from lv_termine_ex where fsid=%s""", (idkey,))   
        rows = cursor.fetchall()
        event_tmp = events[idkey]
        for dateSingle in rows:
                dateElem = {}
                dateElem['StartHour'] = dateSingle[0]
                dateElem['StartMinute'] = dateSingle[1]
                dateElem['EndHour'] = dateSingle[2]
                dateElem['EndMinute'] = dateSingle[3]
                dateElem['StartDate'] = dateSingle[4]
                dateElem['EndDate'] = dateSingle[5]
                dateElem['Room'] = dateSingle[6]
                dateElem['Day'] = dateSingle[7]
                dateElem['Type'] = dateSingle[8]
                li.append(dateElem)
        event_tmp['Date'] = li
        events[idkey] = event_tmp
        li = []
        #dateElem = {}
                       
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#find faculty's unique ID  
    for idkey in module:
        cursor.execute ("""select ModulName,ModulKennung from lv_findet_statt_ex fs join lv_module
        m on fs.IDModulDrehscheibe=m.IDModulDrehscheibe where fs.ID=%s""", (idkey,))   
        rows = cursor.fetchall()
        event_tmp = events[idkey]
        event_tmp['Module'] = rows
        events[idkey] = event_tmp
 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#print to stdio?   
    printDict = True
    if printDict == True:      
        for i, j in events.iteritems(): 
            print "ID: ", i
            for u,v in j.iteritems():
                print u, "<-->", v, "\n"
    
    cursor.close()
    db.close()
    return events
