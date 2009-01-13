#!/usr/bin/python

import sys
import mechanize
from mechanize._util import isstringlike
from mechanize._request import Request
import time
from sys import argv
import MySQLdb

#some defines, change in common.py
from infnine.data.common import templateFile, destinationFile

#print "Drehscheibe/Interface by Dominik Jain"
#print "arguments: %s" % str(argv)
#
#print "initializing mechanize..."

cookies = mechanize.CookieJar()
opener = mechanize.build_opener(mechanize.HTTPCookieProcessor(cookies))
opener.addheaders = [("User-agent", "Mozilla/5.0 (compatible; MyProgram/0.1)")]
mechanize.install_opener(opener)

req = None

class MyBrowser(mechanize.Browser):
    def __init__(self):
        mechanize.Browser.__init__(self)


def writef(buf):
    f=file("debug.html","w")
    f.write(buf)
    f.close()
    
def utf8(s):
	''' converts from latin-1 to utf-8 '''
	return unicode(s, "iso-8859-1").encode("utf-8")

def utf8a(s):
  	return s.encode( "utf-8" )

import os

def createTexFile(thesistype, supervisor, professor, email, title, overview, tasks, prerequisites, url):#, image):
    
    template = open(templateFile, "r")
    
    output=[]
    for line in template :
        line = line.replace('PLACEHOLDER_TYPE', thesistype)
        line = line.replace('PLACEHOLDER_SUPERVISOR', supervisor)
        line = line.replace('PLACEHOLDER_PROFESSOR', professor)
        line = line.replace('PLACEHOLDER_EMAIL', email)
        line = line.replace('PLACEHOLDER_TITLE', title)
        line = line.replace('PLACEHOLDER_OVERVIEW', overview)
        line = line.replace('PLACEHOLDER_TASK', tasks)
        line = line.replace('PLACEHOLDER_PREREQUISITES', prerequisites)
        line = line.replace('PLACEHOLDER_URL', url)
        #line = line.replace('PLACEHOLDER_IMAGE', image)
        output.append(line)
    template.close()
        
    outfile = open(destinationFile+title.replace(' ', '-').lower()+ ".tex", "w")
    for line in output: 
        outfile.write(line ) 
        
    outfile.close()
# end import_rfid_file   



def sendToDrehscheibe(thesistype, supervisor, professor, email, title, overview, tasks, prerequisites, url):

    br = MyBrowser()
    br.set_handle_robots(False)
    
    # login to the drehscheibe
    #print "logging in to www.in.tum.de..."
    br.open("https://www.in.tum.de/login.html.de")
    br.select_form("loginForm")
    br['luserlogin'] = 'MYTUM_USER'
    br['luserpw'] = 'MYTUM_PWD'
    response = br.submit()
    
    # fill in form data
    br.open("https://www.in.tum.de/myintum/item_verwaltung.html.de?createitem=1&itemclass="+thesistype)
    br.form = br.forms().next()
    br["title_de"] = title
    br["content_de"] = "<b>&Uuml;berblick:</b><p>" + overview +"</p><p>"+ tasks +"</p><p>"+ prerequisites +"</p>"
    br["Aufgabensteller"] = professor
    br["Betreuer"] = supervisor + ", (" + email + ")"
    br["categories"] = ["24","97","25"] # Bachelor, Master, Diplom
    br["url"] = url
    t = time.time() + 6*30*24*3600 # ~ six months from now
    br["expirationtime"] = time.strftime("%d.%m.%Y %H:%M", time.localtime(t))
    
    print br
    #response = br.submit()


# --- MAIN APP ---



########################################################################
# 
# Send the information to the Drehscheibe and create the LATEX file
# 
# thesistype    - List of Entries from the "select multiple" field (e.g. ("Diploma Thesis", "HiWi"))
# supervisor    - normal full Name, e.g. "Moritz Tenorth"
# professor     - normal full Name including title, e.g. "Prof. Michael Beetz, PhD."
# email         - email address of the supervisor, e.g. "tenorth@cs.tum.edu"
# title         - title of the thesis
# overview      - short overview of the project 
# tasks         - task description
# prerequisites - text describing the prerequisites
# url           - URL to more information
# image         - file name of an image illustrating the task
#
########################################################################



def publishStudentProject1(thesistype, supervisor, professor, email, title, overview, tasks, prerequisites, url):#, image):
    
    if(("SEP" in thesistype) or ("IDP" in thesistype)):
        
        prefix=""
        if (("SEP" in thesistype) and ("IDP" in thesistype)):
            prefix = "SEP/IDP"
        elif("SEP" in thesistype): 
            prefix = "SEP"
        elif("IDP" in thesistype):
            prefix = "IDP"
        
        # send to drehscheibe
        #sendToDrehscheibe("sypro", supervisor, professor, email, prefix +" "+ title, overview, tasks, prerequisites, url)
        
        # create tex file
        createTexFile(prefix, supervisor, professor, email, title, overview, tasks, prerequisites, url)#, image)
        
        
    # send HiWi or final theses as "Diplomarbeit" with different prefixes 
    if(("HiWi" in thesistype) or 
       ("Diploma Thesis" in thesistype) or 
       ("Master Thesis" in thesistype) or 
       ("Bachelor Thesis" in thesistype)):
        
        prefix=""
        print_title=""
        if (("Diploma Thesis" in thesistype) and ("Bachelor Thesis" in thesistype) and ("Master Thesis" in thesistype)):
            prefix = "DA/BA/MA"
            print_title="Diplom-/Bachelor-/Masterarbeit"
        elif("Bachelor Thesis" in thesistype) and ("Master Thesis" in thesistype): 
            prefix = "BA/MA"
            print_title="Bachelor-/Masterarbeit"
        elif("Diploma Thesis" in thesistype) and ("Master Thesis" in thesistype): 
            prefix = "DA/MA"
            print_title="Diplom-/Masterarbeit"
        elif("Diploma Thesis" in thesistype) and ("Bachelor Thesis" in thesistype): 
            prefix = "DA/BA"
            print_title="Diplom-/Bachelorarbeit"
        elif("Diploma Thesis" in thesistype):
            prefix = "DA"
            print_title="Diplomarbeit"
        elif("Bachelor Thesis" in thesistype):
            prefix = "BA"
            print_title="Bachelorarbeit"
        elif("Master Thesis" in thesistype):
            prefix = "MA"
            print_title="Masterarbeit"
            
        if(("HiWi" in thesistype) and prefix!=""):
            prefix = prefix  + "/HiWi"
            print_title=print_title+"/HiWi"
        elif (("HiWi" in thesistype) and prefix==""):
            prefix = "HiWi"
            print_title="HiWi-Job"

        # send to drehscheibe
        #sendToDrehscheibe("da", supervisor, professor, email, prefix +" "+ title, overview, tasks, prerequisites, url)

        # create tex file
        createTexFile(print_title, supervisor, professor, email, title, overview, tasks, prerequisites, url)#, image)




#publishStudentProject(("Diploma Thesis", "Master Thesis"), 
#              "Moritz Tenorth",
#              "Prof. Beetz, Ph.D.",  
#              "tenorth@cs.tum.edu", 
#              "Embedding Conditional Random Fields and Clustering Techniques into a Robot Knowledge Base", 
#              "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ", 
 #             "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ", 
#              "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ", 
#              "http://www9.in.tum.de/people/tenorth/projects",
#              "test.pdf")
    
