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
    
import wikipedia
from lxml import html

from .process import *
from .multimedia import *
from .cl import *
from .mine import *
from .algorithmy import *
from .commands import *

myname = "bob"
username = getpass.getuser()

it = ""

global OUTPUT_CMD
OUTPUT_CMD = 'print(stuff)'
global STARTERS
STARTERS = [
    "and ",
    "hello ",
    "hey ",
    "hi ",
    "so ",
    "there ",
    "will you ",
    "can you ",
    "please ",
    "if you can ",
    "man ",
    "dude ",
    "my guy ",
    ]
global ENDINGS
ENDINGS = [
    " please",
    " thank you",
    " thanks",
    " now",
    " will you",
    " dude",
    " man",
    " my guy",
    " for me",
    " if you can",
    ]
global COMMANDS
COMMANDS = {
    "open ":"command_open",
    "run ":"command_run",
    "execute ":"command_run",
    "exec ":"command_run",
    "call ":"command_run",
    "launch app ":"command_run",
    "launch ":"command_run",
    "edit ":"command_edit",

    "create templates ":"command_create",
    "move ":"command_move",
    "read ":"command_read",
    "create ":"command_mkdir",
    "delete ":"command_delete",
    
    "play ":"command_play",

    "google for ":"command_google",
    "google ":"command_google",

    "change directory to ":"command_cd",
    "change directory ":"command_cd",
    "cd to ":"command_cd",
    "cd ":"command_cd",
    }
def printbob(stuff):
    global OUTPUT_CMD
    exec( OUTPUT_CMD )
    
    
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
        #printbob("1")
        if istime(output) == True:
            #printbob("3")
            rtype = "time1"
    if rtype == "loc2":
        #printbob("2")
        if istime(output) == True:
            #printbob("4")
            rtype = "time2"
            
    if rtype == "def1":
        info[x] = output
        info[x] = q_t1_proc(output)
    if rtype == "def2":
        info_was[x] = output
        info_was[x] = q_t1_proc(output)
    if rtype == "loc1":
        location[x] = output
        location[x] = q_t1_proc(output)
    if rtype == "loc2":
        location_was[x] = output
        location_was[x] = q_t1_proc(output)
    if rtype == "time1":
        time[x] = output
        time[x] = q_t1_proc(output)
    if rtype == "time2":
        time_was[x] = output
        time_was[x] = q_t1_proc(output)

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
        printbob(x.replace("$$@#¬¬¬"," ")[1:-1])
    return

        
print("---->Made using the amazing Bob-api that was created by Adrian Gjonca\n---->Bob-api is licensed using the: GNU General Public License v3.0")
        
info = {
        "you": "I'm Bob! I'm great Thanks!",
        "your name": "I'm Bob and i must be "+username+".",
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
    
  
print()

os.chdir(str(Path.home()))


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
            x = wikipedia.search(inp)
            printbob("Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\nDo you want me to check?")
            y = input("?> ")

            if "yes" in y.lower():
                printbob("\n"+wikipedia.summary(x[0]))
                y = input("\nI can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " is " + wikipedia.summary(x[0]))
                    printbob("\n"+"All done!")
            else:
                printbob("How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    printbob("\n"+wikipedia.summary(x[1]))
                    y = input("\nI can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " is " + wikipedia.summary(x[0]))
                        printbob("\n"+"All done!")
                    else:
                        printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
                else:
                    printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "def2":
        if key in info_was:
            output = info_was[key]
        elif proc in info_was:
            output = info_was[proc]
        elif search_dict(proc, info_was) != None:
            x = search_dict(proc, info_was)
            output = info_was[x]
        else:
            x = wikipedia.search(inp)
            printbob("Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\nDo you want me to check?")
            y = input("?> ")

            if "yes" in y.lower():
                printbob("\n"+wikipedia.summary(x[0]))
                y = input("\nI can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " was " + wikipedia.summary(x[0]))
                    printbob("\n"+"All done!")
            else:
                printbob("How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    printbob("\n"+wikipedia.summary(x[1]))
                    y = input("\nI can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " was " + wikipedia.summary(x[0]))
                        printbob("\n"+"All done!")
                    else:
                        printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
                else:
                    printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "time1":
        if key in time:
            output = time[key]
        elif proc in time:
            output = time[proc]
        elif search_dict(proc, time) != None:
            x = search_dict(proc, time)
            output = time[x]
        else:
            x = wikipedia.search(inp)
            printbob("Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\nDo you want me to check?")
            y = input("?> ")

            if "yes" in y.lower():
                printbob("\n"+wikipedia.summary(x[0]))
                y = input("\nI can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " is on " + wikipedia.summary(x[0]))
                    printbob("\n"+"All done!")
            else:
                printbob("How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    printbob("\n"+wikipedia.summary(x[1]))
                    y = input("\nI can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " is on " + wikipedia.summary(x[0]))
                        printbob("\n"+"All done!")
                    else:
                        printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
                else:
                    printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "time2":
        if key in time_was:
            output = time_was[key]
        elif proc in time_was:
            output = time_was[proc]
        elif search_dict(proc, time_was) != None:
            x = search_dict(proc, time_was)
            output = time_was[x]
        else:
            x = wikipedia.search(inp)
            printbob("Sorry I don't know anything about "+proc+" but I know a wikipedia page called '"+x[0]+"' which might have what you are asking me for.\nDo you want me to check?")
            y = input("?> ")

            if "yes" in y.lower():
                printbob("\n"+wikipedia.summary(x[0]))
                y = input("\nI can remember that for next time if you like?\n?> ")
                if "yes" in y.lower():
                    remember(key + " was on " + wikipedia.summary(x[0]))
                    printbob("\n"+"All done!")
            else:
                printbob("How about '"+x[1]+"'?")
                y = input("?> ")
                if "yes" in y.lower():
                    printbob("\n"+wikipedia.summary(x[1]))
                    y = input("\nI can remember that for next time if you like?\n?> ")
                    if "yes" in y.lower():
                        remember(key + " was on " + wikipedia.summary(x[0]))
                        printbob("\n"+"All done!")
                    else:
                        printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
                else:
                    printbob("*sigh*\nI give up. Go look it up on google or sonthing then tell me about it when you get back...")
    elif type == "loc1":
        if key in location:
            output = location[key]
        elif proc in location:
            output = location[proc]
        elif search_dict(proc, location) != None:
            x = search_dict(proc, location)
            output = location[x]
        else:
            printbob("Do I look like Siri to you?")
            printbob("Ok I will do it...")
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
            printbob("Do I look like Siri to you?")
            printbob("Ok I will do it...")
            google_com(inp,inp)
    say(output)
    

########################################Main Loop###################################################################################################################
def BOB(IN):
    
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
            
    dynamics2 = {"time":"quarter to nine"}
    for key, value in dynamics.items():
        dynamics2[key] = eval(value)
    info.update(dynamics2)
    
    text = ""
    try:
        text = IN
    except KeyboardInterrupt:
        text = " "
    except EOFError:
        text = " "
    nocap = text
    text = text.lower()


    global STARTERS
    global ENDINGS
    STARTERS.append(myname+" ")
    ENDINGS.append(" "+myname)
    while text.startswith(tuple(STARTERS)):
        for item in STARTERS:
            if text.startswith(item):
                text = text[len(item):]
    while text.endswith(tuple(ENDINGS)):
        for item in ENDINGS:
            if text.endswith(item):
                text = text[:-len(item)]

##This section is about moving words around so bob understands them.
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
        obj = y[0]
        z = x[len(obj)+1:]
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
    if text.startswith("who ") and (not(text.startswith("who is "))) and (not(text.startswith("who am "))) and (not(text.startswith("who are "))) and (not(text.startswith("who was "))) and (not(text.startswith("who were "))):
        x = text[4:]
        y = x.split(' ')
        obj = y[0]
        z = x[len(obj)+1:]
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
    if text.startswith("where ") and (not(text.startswith("where is "))) and (not(text.startswith("where am "))) and (not(text.startswith("where are "))) and (not(text.startswith("where was "))) and (not(text.startswith("where were "))):
        x = text[6:]
        y = x.split(' ')
        obj = y[0]
        z = x[len(obj)+1:]
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
    if text.startswith("when ") and (not(text.startswith("when is "))) and (not(text.startswith("when am "))) and (not(text.startswith("when are "))) and (not(text.startswith("when was "))) and (not(text.startswith("when were "))):
        x = text[5:]
        y = x.split(' ')
        obj = y[0]
        z = x[len(obj)+1:]
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

##This is the heart of the program where questions are answered.
    if text.startswith("what ") or text.startswith("who ") or text.startswith("where ") or text.startswith("when ") or text.startswith("how "):
        query(text)
                 
    elif text[0:findnth(text," ",6)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",6)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",6)] + ' ")')
    elif text[0:findnth(text," ",5)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",5)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",5)] + ' ")')
    elif text[0:findnth(text," ",4)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",4)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",4)] + ' ")')
    elif text[0:findnth(text," ",3)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",3)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",3)] + ' ")')
    elif text[0:findnth(text," ",2)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",2)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",2)] + ' ")')
    elif text[0:findnth(text," ",1)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",1)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",1)] + ' ")')
    elif text[0:findnth(text," ",0)]+" " in COMMANDS:
        exec(COMMANDS[text[0:findnth(text," ",0)]+" "] + "(text,nocap," + '"' + text[0:findnth(text," ",0)] + ' ")')
        
    elif text.startswith("a joke"):
        printbob("You are a joke...")
    elif text.startswith("roll a dice"):
        printbob("Here you go: "+str(random.randint(1, 6)))

    elif text.startswith("exit"):
        exit()
    elif text.startswith("bye"):
        exit()
    elif text.startswith("goodbye"):
        exit()
    elif text.startswith("quit"):
        exit()

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
        
    #Add command
    elif text.startswith("to do "):
        try:
            data3 = open(str(Path.home())+"/"+".commands.bob", 'r').read()
            commands = eval(data3)
        except FileNotFoundError:
            printbob("[BOB] No Commands file availiable. Creating new one")

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


    #Statement
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
        
    #Else
    else:
        say("Sorry //2*1 dont understant how to "+ text + ".")
        print("'"+text[0:findnth(text," ",1)]+" "+"'")

##Saving
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



    

