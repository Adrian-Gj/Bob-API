from datetime import date
import calendar
import os
from datetime import datetime
import random
import json
from pathlib import Path
import sys
import getpass
import shutil
import subprocess
import random
from random import randrange
import requests
from time import sleep
from time import time as timé
    
import libs.wikipedia
from libs.lxml import html

from process import *
from multimedia import *
from cl import *
from mine import *
from algorithmy import *

myname = "bob"
username = getpass.getuser()

it = ""

def remember(text):
    global it
    thing = "x"
    rtype = "x"
    x=0
    y=0
    if text.find(' is in ')>0:
        x = text.find(' is in ')+7
        y = text.find(' is in ')
        thing = "is in"
        rtype = "loc1"
    elif text.find(' is at ')>0:
        x = text.find(' is at ')+7
        y = text.find(' is at ')
        thing = "is at" 
        rtype = "loc1"
    elif text.find(' is on ')>0:
        x = text.find(' is on ')+7
        y = text.find(' is on ')
        thing = "is on" 
        rtype = "loc1"
    elif text.find(' was in ')>0:
        x = text.find(' was in ')+8
        y = text.find(' was in ')
        thing = "was in"
        rtype = "loc2"
    elif text.find(' was at ')>0:
        x = text.find(' was at ')+8
        y = text.find(' was at ')
        thing = "was at"
        rtype = "loc2"
    elif text.find(' is ')>0:
        x = text.find(' is ')+4
        y = text.find(' is ')
        thing = "is"
        rtype = "def1"
    elif text.find(' am ')>0:
        x = text.find(' am ')+4
        y = text.find(' am ')
        thing = "am"
        rtype = "def1"
    elif text.find(' are ')>0:
        x = text.find(' are ')+5
        y = text.find(' are ')
        thing = "are"
        rtype = "def1"
    elif text.find(' was ')>0:
        x = text.find(' was ')+5
        y = text.find(' was ')
        thing = "was"
        rtype = "def2"
    elif text.find(' were ')>0:
        x = text.find(' were ')+6
        y = text.find(' were ')
        thing = "were"
        rtype = "def2"


    input = text[:y]
    output = text[x:]
    if input == "it" or input == "they":
        x = it
    else:
        x = input

    if output.startswith("also "):
        output = info[x]+" "+output

    if rtype == "loc1":
        #print("1")
        if istime(output) == True:
            #print("3")
            rtype = "time1"
    if rtype == "loc2":
        #print("2")
        if istime(output) == True:
            #print("4")
            rtype = "time2"
            
    if rtype == "def1":
        info[x] = output
    if rtype == "def2":
        info_was[x] = output
    if rtype == "loc1":
        location[x] = output
    if rtype == "loc2":
        location_was[x] = output
    if rtype == "time1":
        time[x] = output
    if rtype == "time2":
        time_was[x] = output

    if input != "it":
        it = input
    if input != "they":
        it = input

    x = text
    x = x.replace("the ", "")
    x = x.replace("current ", "")
    x = x.replace("value of ", "")
    return x
def say( str ):
    "This processes text to be said"
    x = " "+str+" "
    x = x.replace(" you are ", " //1*1 ")
    x = x.replace(" i am ", " //1*2 ")
    
    x = x.replace(" you ", " //2*1 ")
    x = x.replace(" i ", " //2*2 ")

    x = x.replace(" your ", " //3*1 ")
    x = x.replace(" my ", " //3*2 ")
	
    x = x.replace(" yourself ", " //4*1 ")
    x = x.replace(" myself ", " //4*2 ")
    
    #
    x = x.replace("//1*1", "I am")
    x = x.replace("//1*2", "you are")
    
    x = x.replace("//2*1", "I")
    x = x.replace("//2*2", "you")

    x = x.replace("//3*1", "my")
    x = x.replace("//3*2", "your")
	
    x = x.replace("//4*1", "myself")
    x = x.replace("//4*2", "yourself")
    if "%SEARCH%" in str:
        google(str.replace("%SEARCH%",""))
    else:
        print(x.replace("$$@#¬¬¬"," "))
    return

        
print("Bob Shell version 1.0")
        
info = {
        "you": "I'm Bob! I'm great Thanks!",
        "your name": "I'm Bob and i must be Adrian.",
        }
info_was = {
        }

location = {
        }
location_was = {
        }

time = {
        }
time_was = {"you born":"abc"
        }

sims = {
        }

commands = {'say': 'echo',
            'echo': 'echo',
            }

dynamics = {"time": "str(datetime.now())",
            "day": "calendar.day_name[date.today().weekday()]",
            "year": "str(datetime.now())",
            "date": "str(datetime.now())",
            "weather": "\"%SEARCH%what is the weather\"",
            "weather like": "\"%SEARCH%what is the weather\"",
            "directory":"os.getcwd()",
            "my directory": "os.getcwd()",
            "in my directory": "'\\n'+str(os.listdir(os.getcwd())).replace(',' , '\\n').replace('[' , ' ').replace(']' , ' ').replace('\\\'' , '')+'\\n'",
            "contents of my directory": "'\\n'+str(os.listdir(os.getcwd())).replace(',' , '\\n').replace('[' , ' ').replace(']' , ' ').replace('\\\'' , '')+'\\n'",
            }


try:
    data = open(str(Path.home())+"/"+".info.bob", 'r').read()
    info = eval(data)
except FileNotFoundError:
    print("[BOB] No Info file availible. Creating new one.")

try:
    data = open(str(Path.home())+"/"+".info_was.bob", 'r').read()
    info_was = eval(data)
except FileNotFoundError:
    print("[BOB] No Info(Was) file availible. Creating new one.")

try:
    data = open(str(Path.home())+"/"+".location.bob", 'r').read()
    location = eval(data)
except FileNotFoundError:
    print("[BOB] No Location file availible. Creating new one.")

try:
    data = open(str(Path.home())+"/"+".location_was.bob", 'r').read()
    location_was = eval(data)
except FileNotFoundError:
    print("[BOB] No Location(Was) file availible. Creating new one.")

try:
    data = open(str(Path.home())+"/"+".time.bob", 'r').read()
    time = eval(data)
except FileNotFoundError:
    print("[BOB] No Location file availible. Creating new one.")

try:
    data = open(str(Path.home())+"/"+".time_was.bob", 'r').read()
    time_was = eval(data)
except FileNotFoundError:
    print("[BOB] No Location file availible. Creating new one.")

    
#try:
#    data2 = open(str(Path.home())+"/"+".sims.bob", 'r').read()
#    sims = eval(data2)
#except FileNotFoundError:
#    print("[BOB] No Sims file availible. Creating new one.")

try:
    data3 = open(str(Path.home())+"/"+".commands.bob", 'r').read()
    commands = eval(data3)
except FileNotFoundError:
    print("[BOB] No Installed Commands Availible. Runnig without commands.")

try:
    data4 = open(str(Path.home())+"/"+".dynamics.bob", 'r').read()
    dynamics = eval(data4)
except FileNotFoundError:
    print("[BOB] No Dynamics file availiable. Using defaults")
    
#try:
#    data5 = open(str(Path.home())+"/"+".dynamics_sims.bob", 'r').read()
#    dynamics_sims = eval(data5)
#except FileNotFoundError:
#    print("[BOB] No Dynamics-Sims file availiable. Using defaults")
    
print()
say("Hello I'm Bob!")

os.chdir(str(Path.home()))

if "@@2&*$£DASNNNOOOó" in info:
    if info["@@2&*$£DASNNNOOOó"] == "Meow":
        print("\n\n\n\n\n\n\n the fox says meow...\n\n\n\n\n\n\n")
        info["@@2&*$£DASNNNOOOó"] = "Woof"
lastloc = "london"

########################################Queries####################################################################################################################
def query(inp):
    proc = q_split(inp)
    type = q_type(inp)
    key = q_t1_proc(proc)
    output = ""
    if type == "def1":
        if key in info:
            output = info[key]
        elif proc in info:
            output = info[proc]
        elif search_dict(proc, info) != None:
            x = search_dict(proc, info)
            output = info[x]
        else:
            x = libs.wikipedia.search(nocap)
            print(" Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\n Do you want me to check?")
            y = input("?> ")
            if "yes" in y.lower():
                print("\n"+libs.wikipedia.summary(x[0]))
                y = input("\n I can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " is " + libs.wikipedia.summary(x[0]))
                    print("\n"+" All done!")
            else:
                print(" How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    print("\n"+libs.wikipedia.summary(x[1]))
                    y = input("\n I can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " is " + libs.wikipedia.summary(x[0]))
                        print("\n"+" All done!")
                    else:
                        print(" *sigh*\n I give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "def2":
        if key in info_was:
            output = info_was[key]
        elif proc in info_was:
            output = info_was[proc]
        elif search_dict(proc, info_was) != None:
            x = search_dict(proc, info_was)
            output = info_was[x]
        else:
            x = libs.wikipedia.search(nocap)
            print(" Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\n Do you want me to check?")
            y = input("?> ")
            if "yes" in y.lower():
                print("\n"+libs.wikipedia.summary(x[0]))
                y = input("\n I can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " was " + libs.wikipedia.summary(x[0]))
                    print("\n"+" All done!")
            else:
                print(" How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    print("\n"+libs.wikipedia.summary(x[1]))
                    y = input("\n I can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " was " + libs.wikipedia.summary(x[0]))
                        print("\n"+" All done!")
                    else:
                        print(" *sigh*\n I give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "time1":
        if key in time:
            output = time[key]
        elif proc in time:
            output = time[proc]
        elif search_dict(proc, time) != None:
            x = search_dict(proc, time)
            output = time[x]
        else:
            x = libs.wikipedia.search(nocap)
            print(" Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\n Do you want me to check?")
            y = input("?> ")
            if "yes" in y.lower():
                print("\n"+libs.wikipedia.summary(x[0]))
                y = input("\n I can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " is on " + libs.wikipedia.summary(x[0]))
                    print("\n"+" All done!")
            else:
                print(" How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    print("\n"+libs.wikipedia.summary(x[1]))
                    y = input("\n I can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " is on " + libs.wikipedia.summary(x[0]))
                        print("\n"+" All done!")
                    else:
                        print(" *sigh*\n I give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "time2":
        if key in time_was:
            output = time_was[key]
        elif proc in time_was:
            output = time_was[proc]
        elif search_dict(proc, time_was) != None:
            x = search_dict(proc, time_was)
            output = time_was[x]
        else:
            x = libs.wikipedia.search(nocap)
            print(" Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\n Do you want me to check?")
            y = input("?> ")
            if "yes" in y.lower():
                print("\n"+libs.wikipedia.summary(x[0]))
                y = input("\n I can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " was on " + libs.wikipedia.summary(x[0]))
                    print("\n"+" All done!")
            else:
                print(" How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    print("\n"+libs.wikipedia.summary(x[1]))
                    y = input("\n I can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " was on " + libs.wikipedia.summary(x[0]))
                        print("\n"+" All done!")
                    else:
                        print(" *sigh*\n I give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "loc1":
        if key in location:
            output = location[key]
        elif proc in location:
            output = location[proc]
        elif search_dict(proc, location) != None:
            x = search_dict(proc, location)
            output = location[x]
        else:
            print(" Do I look like Siri to you?")
            print(" Ok I will do it...")
            google_com(inp,inp)
    elif type == "loc2":
        if key in location_was:
            output = location_was[key]
        elif proc in location_was:
            output = location_was[proc]
        elif search_dict(proc, location) != None:
            x = search_dict(proc, location)
            output = location[x]
        else:
            print(" Do I look like Siri to you?")
            print(" Ok I will do it...")
            google_com(inp,inp)
    say(output)
    

########################################Main Loop###################################################################################################################
while True:
    info["up"]="the sky"
    
    try:
        data4 = open(str(Path.home())+"/"+".dynamics.bob", 'r').read()
        dynamics = eval(data4)
    except FileNotFoundError:
        eval("\" \"")

    try:
        data3 = open(str(Path.home())+"/"+".commands.bob", 'r').read()
        commands = eval(data3)
    except FileNotFoundError:
        eval("\" \"")
        
    #try:
    #    data5 = open(str(Path.home())+"/"+".dynamics_sims.bob", 'r').read()
    #    dynamics_sims = eval(data5)
    #except FileNotFoundError:
    #    eval("\" \"")
    
    dynamics2 = {"time":"quarter to nine"}
    for key, value in dynamics.items():
        dynamics2[key] = eval(value)
    info.update(dynamics2)   
    #sims.update(dynamics_sims)
    try:
        text = input(os.getcwd()+"> ")
    except KeyboardInterrupt:
        text = " "
    except EOFError:
        text = " "
    nocap = text
    text = text.lower()


    #Stuff to add
    Greeting = False
    
    #Word Starters
    while text.startswith(myname+" ") or text.startswith("hello ") or text.startswith("hey ") \
        or text.startswith("hi ") or text.startswith("so ") or text.startswith("there ") \
        or text.startswith("will you ") or text.startswith("can you ") or text.startswith("please ")\
        or text.startswith("if you can ") or text.startswith("man ") or text.startswith("dude ") or text.startswith("my guy ")\
        or text.startswith("if you do not mind "):
        if text.startswith(myname+" "):
            text = text[len(myname)+1:]
            nocap = nocap[len(myname)+1:]
        if text.startswith("hello "):
            text = text[6:]
            nocap = nocap[6:]
            Greeting = True
        if text.startswith("hey "):
            text = text[4:]
            nocap = nocap[4:]
            Greeting = True
        if text.startswith("hi "):
            text = text[3:]
            nocap = nocap[3:]
            Greeting = True
        if text.startswith("so "):
            text = text[3:]
            nocap = nocap[3:]
        if text.startswith("there "):
            text = text[6:]
            nocap = nocap[6:]
        if text.startswith("will you "):
            text = text[9:]
            nocap = nocap[9:]
        if text.startswith("can you "):
            text = text[8:]
            nocap = nocap[8:]
        if text.startswith("please "):
            text = text[7:]
            nocap = nocap[7:]
        if text.startswith("if you can "):
            text = text[11:]
            nocap = nocap[11:]
        if text.startswith("man "):
            text = text[4:]
            nocap = nocap[4:]
        if text.startswith("dude "):
            text = text[5:]
            nocap = nocap[5:]
        if text.startswith("my guy "):
            text = text[7:]
            nocap = nocap[7:]
        if text.startswith("if you do not mind "):
            text = text[19:]
            nocap = nocap[19:]
            
    #Word endings
    while text.endswith(" "+myname) or text.endswith(" please") or text.endswith(" thank you")\
        or text.endswith(" thanks") or text.endswith(" now") or text.endswith(" will you")\
        or text.endswith(" dude") or text.endswith(" man") or text.endswith(" my guy")\
        or text.endswith(" for me"):
        if text.endswith(" "+myname):
            text = text[:len(text)-4]
            nocap = nocap[:len(nocap)-4]
        if text.endswith(" please"):
            text = text[:len(text)-7]
            nocap = nocap[:len(nocap)-7]
        if text.endswith(" thank you"):
            text = text[:len(text)-10]
            nocap = nocap[:len(nocap)-10]
        if text.endswith(" thanks"):
            text = text[:len(text)-7]
            nocap = nocap[:len(nocap)-7]
        if text.endswith(" now"):
            text = text[:len(text)-4]
            nocap = nocap[:len(nocap)-4]
        if text.endswith(" will you"):
            text = text[:len(text)-9]
            nocap = nocap[:len(nocap)-9]
        if text.endswith(" dude"):
            text = text[:len(text)-5]
            nocap = nocap[:len(nocap)-5]
        if text.endswith(" man"):
            text = text[:len(text)-4]
            nocap = nocap[:len(nocap)-4]
        if text.endswith(" my guy"):
            text = text[:len(text)-7]
            nocap = nocap[:len(nocap)-7]
        if text.endswith(" for me"):
            text = text[:len(text)-7]
            nocap = nocap[:len(nocap)-7]


    #Reply to stuff
    if Greeting:
        print(" Hi "+username+"!")
        
    #Remove and
    if text.startswith("and "):
        text = text[4:]
        nocap = nocap[4:]

    
########################################################Section 2#########################################################################################################

##########SEMI_PROCESS#########
    if text.startswith("what ") and text.endswith(" is"):
        x = text[5:len(text)-3]
        text = "what is "+x
    if text.startswith("what ") and text.endswith(" was"):
        x = text[5:len(text)-4]
        text = "what was "+x        
    if text.startswith("who ") and text.endswith(" is"):
        x = text[4:len(text)-3]
        text = "who is "+x        
    if text.startswith("who ") and text.endswith(" was"):
        x = text[4:len(text)-4]
        text = "who was "+x
    if text.startswith("where ") and text.endswith(" is"):
        x = text[6:len(text)-3]
        text = "where is "+x
    if text.startswith("where ") and text.endswith(" was"):
        x = text[6:len(text)-4]
        text = "where was "+x        
    if text.startswith("when ") and text.endswith(" is"):
        x = text[5:len(text)-3]
        text = "when is "+x        
    if text.startswith("when ") and text.endswith(" was"):
        x = text[5:len(text)-4]
        text = "when was "+x

    
    if text.startswith("what ") and " is it" in text:
        if " is it " in text:
            x = text[5:text.find(" is it ")]
            text = "what is the "+x+text[text.find(" is it ")+6:]
        else:
            x = text[5:len(text)-6]
            text = "what is the "+x
        

    if text.startswith("what ") and (not(text.startswith("what is "))) and (not(text.startswith("what does "))) and (not(text.startswith("what am "))) and (not(text.startswith("what are "))) and (not(text.startswith("what was "))) and (not(text.startswith("what were "))):
        x = text[5:]
        y = x.split(' ')
        #print(y[0])
        obj = y[0]
        z = x[len(obj)+1:]
        #print(z)

        type = " is "
        if " is " in text:
            type=" is "
        elif " am " in text:
            type=" am "
        elif " are " in text:
            type=" are "
        elif " was " in text:
            type=" was "
        elif " were " in text:
            type=" were "
        text = "what"+type+obj+" that "+z
        #print(text)
    if text.startswith("who ") and (not(text.startswith("who is "))) and (not(text.startswith("who am "))) and (not(text.startswith("who are "))) and (not(text.startswith("who was "))) and (not(text.startswith("who were "))):
        x = text[4:]
        y = x.split(' ')
        #print(y[0])
        obj = y[0]
        z = x[len(obj)+1:]
        #print(z)

        type = " is "
        if " is " in text:
            type=" is "
        elif " am " in text:
            type=" am "
        elif " are " in text:
            type=" are "
        elif " was " in text:
            type=" was "
        elif " were " in text:
            type=" were "
        text = "who"+type+obj+" that "+z
        #print(text)
    if text.startswith("where ") and (not(text.startswith("where is "))) and (not(text.startswith("where am "))) and (not(text.startswith("where are "))) and (not(text.startswith("where was "))) and (not(text.startswith("where were "))):
        x = text[6:]
        y = x.split(' ')
        #print(y[0])
        obj = y[0]
        z = x[len(obj)+1:]
        #print(z)

        type = " is "
        if " is " in text:
            type=" is "
        elif " are " in text:
            type=" are "
        elif " was " in text:
            type=" was "
        elif " were " in text:
            type=" were "
        text = "where"+type+obj+" that "+z
        #print(text)
    if text.startswith("when ") and (not(text.startswith("when is "))) and (not(text.startswith("when am "))) and (not(text.startswith("when are "))) and (not(text.startswith("when was "))) and (not(text.startswith("when were "))):
        x = text[5:]
        y = x.split(' ')
        #print(y[0])
        obj = y[0]
        z = x[len(obj)+1:]
        #print(z)

        type = " is "
        if " is " in text:
            type=" is "
        elif " am " in text:
            type=" am "
        elif " are " in text:
            type=" are "
        elif " was " in text:
            type=" was "
        elif " were " in text:
            type=" were "
        text = "when"+type+obj+" that "+z
        #print(text)
####loc
    if text.startswith("i am in "):
        lastloc = text[8:].lower()
        location["i"] = lastloc
    elif text.startswith("we are in "):
        lastloc = text[10:].lower()
        location["i"] = lastloc
    elif text.startswith("i am currently in "):
        lastloc = text[8:].lower()
        location["i"] = lastloc
    elif text.startswith("we are currently in "):
        lastloc = text[10:].lower()
        location["i"] = lastloc
    elif text.startswith("i am now in "):
        lastloc = text[8:].lower()
        location["i"] = lastloc
    elif text.startswith("we are now in "):
        lastloc = text[10:].lower()
        location["i"] = lastloc

#####Question
    elif text.startswith("what does the fox say"):
        sleep(4)
        print(" fó× you!")
        sleep(2)
        print(" Absolute fó×íΠ֍ fó×é®!")
        sleep(2)
        print(" I FÓ×ÍΠ֍ HATE YOU!")
        sleep(2)
        info["@@2&*$£DASNNNOOOó"] = "Meow"
        starttime=timé()
        while timé()-starttime < 5:
            print("ééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééé")
        f = open(str(Path.home())+"/"+".info.bob","w")
        f.write( str(info) )
        f.close()
        exit()
        
    elif text.startswith("what ") or text.startswith("who ") or text.startswith("where ") or text.startswith("when ") or text.startswith("how "):
        query(text)
            
#####Basic Commands        
    elif text.startswith("open "):
        text = text[5:]
        nocap = nocap[5:]
        while text.startswith("the ") or text.startswith("file ") or text.startswith("document ") or text.startswith("called ") or text.startswith("app ") or text.startswith("site ") or text.startswith("website ") or text.startswith("program "):
            if text.startswith("the "):
                text = text[4:]
                nocap = nocap[4:]
            if text.startswith("file "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("document "):
                text = text[9:]
                nocap = nocap[9:]
            if text.startswith("called "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith("app "):
                text = text[4:]
                nocap = nocap[4:]
            if text.startswith("site "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("website "):
                text = text[8:]
                nocap = nocap[8:]
            if text.startswith("program "):
                text = text[8:]
                nocap = nocap[8:]
            if text.startswith(' "'):
                break
        try:
            if shutil.which(nocap.replace('"',"")):
                os.system(nocap)
            else:
                open_file(nocap)
        except FileNotFoundError:
            if site_exists("http://"+(nocap.replace("http://","").replace("https://",""))):
                open_file("http://"+(nocap.replace("http://","").replace("https://","")))
            elif site_exists("http://"+(nocap.replace("http://","").replace("https://","")) + ".com"):
                open_file("http://"+(nocap.replace("http://","").replace("https://","")) + ".com")
            else:
                print(" Can't find the specified file/program.")
    elif text.startswith("run "):
        os.system(nocap[4:])
    elif text.startswith("execute "):
        os.system(nocap[8:])
    elif text.startswith("exec "):
        os.system(nocap[5:])
    elif text.startswith("call "):
        os.system(nocap[5:])
    elif text.startswith("launch app "):
        os.system(nocap[11:])
    elif text.startswith("launch "):
        os.system(nocap[7:])

    elif text.startswith("edit "):
        text = text[5:]
        nocap = nocap[5:]
        while text.startswith("the ") or text.startswith("file ") or text.startswith("document ") or text.startswith("called "):
            if text.startswith("the "):
                text = text[4:]
                nocap = nocap[4:]
            if text.startswith("file "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("document "):
                text = text[9:]
                nocap = nocap[9:]
            if text.startswith("called "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith(' "'):
                break
        open_file(nocap)

####Command line
    elif text.startswith("move "):
        text = text[5:]
        nocap = nocap[5:]
        a = nocap[0:text.find("to")-1]
        b = nocap[text.find("to")+3:]
        print(a)
        print(b)
        while a.startswith("file ") or a.startswith("\"") or a.startswith("the ") or a.startswith("called ") or a.startswith("my ")\
              or a.startswith("named ") or a.startswith("directory ") or a.startswith("folder "):
            if a.startswith("\""):
                break;
            if a.startswith("file "):
                a = a[5:]
            if a.startswith("the "):
                a = a[4:]
            if a.startswith("called "):
                a = a[7:]
            if a.startswith("named "):
                a = a[6:]
            if a.startswith("my "):
                a = a[3:]
            if a.startswith("directory "):
                a = a[10:]
            if a.startswith("folder "):
                a = a[7:]
        while b.startswith("file ") or b.startswith("\"") or b.startswith("the ") or b.startswith("called ") or b.startswith("my ")\
              or b.startswith("named ") or b.startswith("directory ") or b.startswith("folder "):
            if b.startswith("\""):
                break;
            if b.startswith("file "):
                b = b[5:]
            if b.startswith("the "):
                b = b[4:]
            if a.startswith("called "):
                b = b[7:]
            if a.startswith("named "):
                b = b[6:]
            if a.startswith("my "):
                b = b[3:]
            if a.startswith("directory "):
                b = b[10:]
            if a.startswith("folder "):
                b = b[7:]
        try:
            shutil.move(a, b)
        except FileNotFoundError:
            print(" I can't find one of the files.")

    elif text.startswith("read "):
        text = text[5:]
        nocap = nocap[5:]
        while text.startswith("file ") or text.startswith("\"") or text.startswith("the ") or text.startswith("called ") or text.startswith("my ")\
              or text.startswith("named ") or text.startswith("directory ") or text.startswith("folder "):
            if text.startswith("\""):
                text = text[1:]
                nocap = nocap[1:]
                break;
            if text.startswith("file "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("the "):
                text = text[4:]
                nocap = nocap[4:]
            if text.startswith("called "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith("named "):
                text = text[6:]
                nocap = nocap[6:]
            if text.startswith("my "):
                text = text[3:]
                nocap = nocap[3:]
            if text.startswith("directory "):
                text = text[10:]
                nocap = nocap[10:]
            if text.startswith("folder "):
                text = text[7:]
                nocap = nocap[7:]
        try:
            data = open(nocap, 'r').read()
            print(data)
        except FileNotFoundError:
            print(" I don't know where \""+nocap+"\" is")
            
    elif text.startswith("create "):
        text = text[7:]
        nocap = nocap[7:]
        x = False
        if text.startswith("a "):
            text = text[2:]
            nocap = nocap[2:]
        if text.startswith("directory "):
            text = text[10:]
            nocap = nocap[10:]
            x = True
        elif text.startswith("folder "):
            text = text[7:]
            nocap = nocap[7:]
            x = True
        while text.startswith("\"") or text.startswith("called ") or text.startswith("named ")\
              or text.startswith("and call it ") or text.startswith("and name it ") or text.startswith("that is "):
            if text.startswith("\""):
                text = text[1:]
                nocap = nocap[1:]
                break;
            if text.startswith("called "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith("named "):
                text = text[6:]
                nocap = nocap[6:]
            if text.startswith("and call it "):
                text = text[12:]
                nocap = nocap[12:]
            if text.startswith("and name it "):
                text = text[12:]
                nocap = nocap[12:]
            if text.startswith("that is "):
                text = text[8:]
                nocap = nocap[8:]
        mkdir(text)
        
    elif text.startswith("delete "):
        text = text[7:]
        nocap = nocap[7:]
        while text.startswith("my ") or text.startswith("\"") or text.startswith("the ")\
              or text.startswith("file ") or text.startswith("called ") or text.startswith("named ")\
              or text.startswith("directory ") or text.startswith("folder ")  or text.startswith("document "):
            if text.startswith("\""):
                text = text[1:]
                nocap = nocap[1:]
                break;
            if text.startswith("the "):
                text = text[4:]
                nocap = nocap[4:]
            if text.startswith("my "):
                text = text[6:]
                nocap = nocap[6:]
            if text.startswith("file "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("called "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith("named "):
                text = text[6:]
                nocap = nocap[6:]
            if text.startswith("directory "):
                text = text[10:]
                nocap = nocap[10:]
            if text.startswith("folder "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith("document "):
                text = text[9:]
                nocap = nocap[9:]
        send2trash.send2trash(nocap)
        
#####Music
    elif text.startswith("play "):
        text = text[5:]
        nocap = nocap[5:]
        while text.startswith("song ") or text.startswith("video ") or text.startswith("my ") or text.startswith("\"")\
              or text.startswith("the ") or text.startswith("file ") or text.startswith("called ") or text.startswith("named "):
            if text.startswith("\""):
                text = text[1:]
                nocap = nocap[1:]
                break;
            if text.startswith("song "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("video "):
                text = text[6:]
                nocap = nocap[6:]
            if text.startswith("the "):
                text = text[4:]
                nocap = nocap[4:]
            if text.startswith("my "):
                text = text[6:]
                nocap = nocap[6:]
            if text.startswith("file "):
                text = text[5:]
                nocap = nocap[5:]
            if text.startswith("called "):
                text = text[7:]
                nocap = nocap[7:]
            if text.startswith("named "):
                text = text[6:]
                nocap = nocap[6:]
        play(nocap)
#####Misc
    elif text.startswith("google for "):
        text = text[11:]
        nocap = nocap[11:]
        google(nocap)
    elif text.startswith("google "):
        text = text[7:]
        nocap = nocap[7:]
        google(nocap)
#####CD
    elif text.startswith("change directory to "):
        try:
            os.chdir(nocap[20:].replace("~",str(Path.home())))
        except FileNotFoundError:
            print(" "+"Sorry but I don't undersand where "+nocap[20:]+" is. Maybe you misspelt something.")
    elif text.startswith("change directory "):
        try:
            os.chdir(nocap[17:].replace("~",str(Path.home())))
        except FileNotFoundError:
            print(" "+"Sorry but I don't undersand where "+nocap[17:]+" is. Maybe you misspelt something.")
    elif text.startswith("cd to "):
        try:
            os.chdir(nocap[6:].replace("~",str(Path.home())))
        except FileNotFoundError:
            print(" "+"Sorry but I don't undersand where "+nocap[6:]+" is. Maybe you misspelt something.")
    elif text.startswith("cd "):
        try:
            os.chdir(nocap[3:].replace("~",str(Path.home())))
        except FileNotFoundError:
            print(" "+"Sorry but I don't undersand where "+nocap[3:]+" is. Maybe you misspelt something.")

#####Jokes
    elif text.startswith("a joke"):
        print(" You are a joke...")
    elif text.startswith("speak a foreign language"):
        print(" Ti je nje idiot.")
    elif text.startswith("speak another language"):
        print(" Me duket si ti vetem shkrove 'another language' per factin te ti sdi si te shcruash 'foreign'.")
    elif text.startswith("roll a dice"):
        print(" Here you go: "+str(random.randint(1, 6)))

#####Exiting
    elif text.startswith("exit"):
        exit()
    elif text.startswith("bye"):
        exit()
    elif text.startswith("goodbye"):
        exit()
    elif text.startswith("quit"):
        exit()

#####Complex Commands
    elif text[0:findnth(text," ",3)] in commands:
        if commands[text[0:findnth(text," ",3)]].startswith(":Python:"):
            exec(commands[text[0:findnth(text," ",3)]][8:].replace("_input_",nocap[findnth(nocap," ",3)+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:findnth(text," ",2)]] + " " + nocap[findnth(nocap," ",2)+1:])
    elif text[0:findnth(text," ",2)] in commands:
        if commands[text[0:findnth(text," ",2)]].startswith(":Python:"):
            exec(commands[text[0:findnth(text," ",2)]][8:].replace("_input_",nocap[findnth(nocap," ",2)+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:findnth(text," ",2)]] + " " + nocap[findnth(nocap," ",2)+1:])
    elif text[0:findnth(text," ",1)] in commands:
        if commands[text[0:findnth(text," ",1)]].startswith(":Python:"):
            exec(commands[text[0:findnth(text," ",1)]][8:].replace("_input_",nocap[findnth(nocap," ",1)+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:findnth(text," ",1)]] + " " + nocap[findnth(nocap," ",1)+1:])
    elif text[0:text.find(" ")] in commands:
        if commands[text[0:text.find(" ")]].startswith(":Python:"):
            exec(commands[text[0:text.find(" ")]][8:].replace("_input_",nocap[nocap.find(" ")+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:text.find(" ")]] + " " + nocap[nocap.find(" ")+1:])
    elif text in commands:
        if commands[text].startswith(":Python:"):
            exec(commands[text][8:].replace("_input_",""))
        else:
            os.system(commands[text])  
        
#####Add command
    elif text.startswith("to do "):
        try:
            data3 = open(str(Path.home())+"/"+".commands.bob", 'r').read()
            commands = eval(data3)
        except FileNotFoundError:
            print("[BOB] No Commands file availiable. Creating new one")

        x = text.find('call')
        y = 4
        if x == -1:
            x = text.find('run')
            y = 3
        if x == -1:
            x = text.find('open')
            y = 4
        if x == -1:
            x = text.find('execute')
            y = 7
        if x == -1:
            x = text.find('exec')
            y = 4

        commands[text[6:x-1]] = text[x+1+y:]
        
        f = open(str(Path.home())+"/"+".commands.bob","w")
        f.write( str(commands) )
        f.close()

#####Creation
    elif text.startswith("create templates "):
        if text[7:].startswith("templates"):
            print("[BOB] [INFO] Creating templates is required to install adons.")
            print("[BOB] [CAUTION] Do not do this if you have previously installed any addons you wish to keep.")
            x = input("[BOB] [???] Do you wish to proceed? ('Yes' to autheticate) \n>>> ")
            if x == "Yes":
                print("[BOB] Creating templates...")
                f = open(str(Path.home())+"/"+".commands.bob","w")
                f.write(str(commands))
                f.close()
                f = open(str(Path.home())+"/"+".dynamics.bob","w")
                f.write(str(dynamics))
                f.close()
                #f = open(str(Path.home())+"/"+".dynamics_sims.bob","w")
                #f.write("{\n\n}")
                #f.close()
                print("\n I have completed the creation of your templates.\n You may now install addons.")

#####Statement
    elif text.startswith("remember that "):
        x = text[14:]
        remember(x)
    elif text.startswith("remember "):
        x = text[9:]
        remember(x)
    elif text.find(" is ") != -1 or text.find(" are ") != -1 or text.find(" am ") != -1:
        x = text
        remember(x)
    elif text.find(" were ") != -1 or text.find(" was ") != -1:
        x = text
        remember(x)
        
#####Else
    else:
        say(" Sorry //2*1 dont understant how to "+ text + ".")

#####Saving################################################################################
    f = open(str(Path.home())+"/"+".info.bob","w")
    f.write( str(info) )
    f.close()

    #a = open(str(Path.home())+"/"+".sims.bob","w")
    #a.write( str(sims) )
    #a.close()

    b = open(str(Path.home())+"/"+".info_was.bob","w")
    b.write( str(info_was) )
    b.close()

    c = open(str(Path.home())+"/"+".location.bob","w")
    c.write( str(location) )
    c.close()

    d = open(str(Path.home())+"/"+".location_was.bob","w")
    d.write( str(location_was) )
    d.close()

    e = open(str(Path.home())+"/"+".time.bob","w")
    e.write( str(time) )
    e.close()

    g = open(str(Path.home())+"/"+".time_was.bob","w")
    g.write( str(time) )
    g.close()

    

