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
import urllib.request
import random
from random import randrange
try:
    import wikipedia
except ImportError:
    print("[BOB] The 'wikipedia' python package is unavaliable. It is required for certain questions.")
    print("[BOB] Installing package")
    os.system("pip install wikipedia")
    import wikipedia
    
try:
    import send2trash
except ImportError:
    print("[BOB] The 'send2trash' python package is unavaliable. It is required for saftey deletes.")
    print("[BOB] Installing package")
    os.system("pip install send2trash")
    import send2trash
myname = "bob"
username = getpass.getuser()

it = ""

def istime(text):
    timepts = 0
    locpts = 0
    if 'noon' in text:
        timepts += 1
    if 'afternoon' in text:
        timepts += 1
    if 'midnight' in text:
        timepts += 1
    if 'th of' in text:
        timepts += 1
    if 'january' in text:
        timepts += 1
    if 'february' in text:
        timepts += 1
    if 'march' in text:
        timepts += 1
    if 'april' in text:
        timepts += 1
    if 'may' in text:
        timepts += 1
    if 'june' in text:
        timepts += 1
    if 'july' in text:
        timepts += 1
    if 'august' in text:
        timepts += 1
    if 'september' in text:
        timepts += 1
    if 'november' in text:
        timepts += 1
    if 'december' in text:
        timepts += 1
    if 'monday' in text:
        timepts += 1
    if 'tuesday' in text:
        timepts += 1
    if 'wednesday' in text:
        timepts += 1
    if 'thursday' in text:
        timepts += 1
    if 'friday' in text:
        timepts += 1
    if 'saturday' in text:
        timepts += 1
    if 'sunday' in text:
        timepts += 1
    if ' day' in text:
        timepts += 5
    if 'day ' in text:
        timepts += 5
    if ' night' in text:
        timepts += 5
    if 'night ' in text:
        timepts += 5
    if text.endswith(" night"):
        timepts += 40
    if text.endswith(" day"):
        timepts += 40
    if text.endswith(" noon"):
        timepts += 30
    if text.endswith(" afternoon"):
        timepts += 30
    if text.endswith(" midnight"):
        timepts += 30
        
    if 'street' in text:
        locpts += 20
    if 'avenue' in text:
        locpts += 20
    if text.endswith(" street"):
        locpts += 40
    if text.endswith(" avenue"):
        locpts += 40

    return timepts>locpts
def remember(text):
    global it
    thing = "is"
    rtype = "def1"
    x=0
    y=0
    if text.find(' is in ')>0:
        x = text.find(' is in ')+7
        y = text.find(' is in ')
        thing = "is in"
        rtype = "loc1"
    if text.find(' is at ')>0:
        x = text.find(' is at ')+7
        y = text.find(' is at ')
        thing = "is at" 
        rtype = "loc1"
    if text.find(' is on ')>0:
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
        print("1")
        if istime(output) == True:
            print("2")
            rtype = "time1"
            
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

    if input != "it":
        it = input
    if input != "they":
        it = input

def q_type(text):
    if text.startswith("what is "):
        return "def1"
    elif text.startswith("what are "):
        return "def1"
    elif text.startswith("what am "):
        return "def1"
    elif text.startswith("what was "):
        return "def2"
    elif text.startswith("what were "):
        return "def2"
    elif text.startswith("who is "):
        return "def1"
    elif text.startswith("who are "):
        return "def1"
    elif text.startswith("what am "):
        return "def1"
    elif text.startswith("who was "):
        return "def2"
    elif text.startswith("who were "):
        return "def2"
    elif text.startswith("when is "):
        return "time1"
    elif text.startswith("when am "):
        return "time1"
    elif text.startswith("when are "):
        return "time1"
    elif text.startswith("what time is "):
        return "time1"
    elif text.startswith("what time am "):
        return "time1"
    elif text.startswith("what time are "):
        return "time1"
    elif text.startswith("where is "):
        return "loc1"
    elif text.startswith("where am "):
        return "loc1"
    elif text.startswith("where was "):
        return "loc2"
    elif text.startswith("how is "):
        return "def1"
    elif text.startswith("how are "):
        return "def1"
    elif text.startswith("how am "):
        return "def1"
    elif text.startswith("how was "):
        return "def2"
    elif text.startswith("how were "):
        return "def2"


def q_split(text):
    x = ""
    if text.startswith("what is "):
        x = text[8:]
    elif text.startswith("what are "):
        x = text[9:]
    if text.startswith("what am "):
        x = text[8:]
    elif text.startswith("what was "):
        x = text[9:]
    elif text.startswith("what were "):
        x = text[10:]
    elif text.startswith("who is "):
        x = text[7:]
    elif text.startswith("who are "):
        x = text[8:]
    elif text.startswith("who am "):
        x = text[7:]
    elif text.startswith("who was "):
        x = text[8:]
    elif text.startswith("who were "):
        x = text[9:]
    elif text.startswith("when is "):
        x = text[8:]
    elif text.startswith("when am "):
        x = text[8:]
    elif text.startswith("when are "):
        x = text[9:]
    elif text.startswith("what time is "):
        x = text[13:]
    elif text.startswith("what time am "):
        x = text[13:]
    elif text.startswith("what time are "):
        x = text[14:]
    elif text.startswith("where is "):
        x = text[9:]
    elif text.startswith("where am "):
        x = text[9:]
    elif text.startswith("where was "):
        x = text[10:]
    elif text.startswith("how is "):
        x = text[7:]
    elif text.startswith("how are "):
        x = text[8:]
    elif text.startswith("how am "):
        x = text[7:]
    elif text.startswith("how was "):
        x = text[8:]
    elif text.startswith("how were "):
        x = text[9:]

    if x == "it":
        x=it
    if x == "they":
        x=it
    return x

def q_t1_proc(text):
    x = text
    x = x.replace("the ", "")
    x = x.replace("current ", "")
    x = x.replace("value of ", "")
    return x
def site_exists(url):
    """
    Checks that a given URL is reachable.
    :param url: A URL
    :rtype: bool
    """
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False
    except urllib.error.URLError:
        return False
    except socket.gaierror:
        return False
def mkdir(name):
    try:
        os.makedirs(name)
    except OSError:
        return 
def copy(src, dst, symlinks=False, ignore=None):
    x = os.path.basename(src)
    y = dst + ""
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join(dst,x), symlinks, ignore)
    else:
        shutil.copy2(src, dst)
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

print("Bob Shell version 1.0")
def play( stri ):
    "Play"
    x = ""
            
    if os.path.isfile(stri):
        open_file(x+stri)
    elif os.path.isfile(str(Path.home())+"/Music/"+stri):
        open_file(x+(str(Path.home())+"/Music/"+stri))
        
    elif os.path.isfile(stri+".mp3"):
        open_file(x+stri+".mp3")
    elif os.path.isfile(str(Path.home())+"/Music/"+stri+".mp3"):
        open_file(x+(str(Path.home())+"/Music/"+stri+".mp3"))

    elif os.path.isfile(stri+".mp2"):
        open_file(x+stri+".mp2")
    elif os.path.isfile(str(Path.home())+"/Music/"+stri+".mp2"):
        open_file(x+(str(Path.home())+"/Music/"+stri+".mp2"))

    elif os.path.isfile(stri+".wav"):
        open_file(x+stri+".wav")
    elif os.path.isfile(str(Path.home())+"/Music/"+stri+".wav"):
        open_file(x+(str(Path.home())+"/Music/"+stri+".wav"))

    elif os.path.isfile(stri+".au"):
        open_file(x+stri+".au")
    elif os.path.isfile(str(Path.home())+"/Music/"+stri+".au"):
        open_file(x+(str(Path.home())+"/Music/"+stri+".au"))

    elif os.path.isfile(stri+".ogg"):
        open_file(x+stri+".ogg")
    elif os.path.isfile(str(Path.home())+"/Music/"+stri+".ogg"):
        open_file(x+(str(Path.home())+"/Music/"+stri+".ogg"))

    elif os.path.isfile(stri+".wma"):
        open_file(x+stri+".wma")
    elif os.path.isfile(str(Path.home())+"/Music/"+stri+".wma"):
        open_file(x+(str(Path.home())+"/Music/"+stri+".wma"))


    elif os.path.isfile(str(Path.home())+"/Videos/"+stri):
        open_file(x+(str(Path.home())+"/Videos/"+stri))
        
    elif os.path.isfile(stri+".mp3"):
        open_file(x+stri+".mp3")
    elif os.path.isfile(str(Path.home())+"/Videos/"+stri+".mp3"):
        open_file(x+(str(Path.home())+"/Videos/"+stri+".mp3"))

    elif os.path.isfile(stri+".mp2"):
        open_file(x+stri+".mp2")
    elif os.path.isfile(str(Path.home())+"/Videos/"+stri+".mp2"):
        open_file(x+(str(Path.home())+"/Videos/"+stri+".mp2"))

    elif os.path.isfile(stri+".wav"):
        open_file(x+stri+".wav")
    elif os.path.isfile(str(Path.home())+"/Videos/"+stri+".wav"):
        open_file(x+(str(Path.home())+"/Videos/"+stri+".wav"))

    elif os.path.isfile(stri+".au"):
        open_file(x+stri+".au")
    elif os.path.isfile(str(Path.home())+"/Videos/"+stri+".au"):
        open_file(x+(str(Path.home())+"/Videos/"+stri+".au"))

    elif os.path.isfile(stri+".ogg"):
        open_file(x+stri+".ogg")
    elif os.path.isfile(str(Path.home())+"/Videos/"+stri+".ogg"):
        open_file(x+(str(Path.home())+"/Videos/"+stri+".ogg"))

    elif os.path.isfile(stri+".wma"):
        open_file(x+stri+".wma")
    elif os.path.isfile(str(Path.home())+"/Videos/"+stri+".wma"):
        open_file(x+(str(Path.home())+"/Videos/"+stri+".wma"))


    else:
        print(" I can find that song...")
        print(str(Path.home())+"/Music/"+stri)

def search(string):
    x = string.split(" ")
    open_file("https://www.google.com/search?q="+string.replace("%","%25").replace("+","%2B").replace(" ","+"))
def say( str ):
    "This processes text to be said"
    x = " "+str+" "
    x = x.replace(" you are ", " //1*1 ")
    x = x.replace(" i am ", " //1*2 ")
    
    x = x.replace(" you ", " //2*1 ")
    x = x.replace(" i ", " //2*2 ")

    x = x.replace(" your ", " //3*1 ")
    x = x.replace(" my ", " //3*2 ")
    
    #
    x = x.replace("//1*1", "I am")
    x = x.replace("//1*2", "you are")
    
    x = x.replace("//2*1", "I")
    x = x.replace("//2*2", "you")

    x = x.replace("//3*1", "my")
    x = x.replace("//3*2", "your")
    
    print(x.replace("$$@#¬¬¬"," "))
    return

info = {
        "you": "Great Thanks!",
        }
info_was = {
        }

location = {
        }
location_was = {
        }

time = {
        }

sims = {
        }

commands = {'say': 'echo',
            'echo': 'echo'}

dynamics = {'time': str(datetime.now()),
            "day": calendar.day_name[date.today().weekday()],
            "year": str(datetime.now()),
            "date": str(datetime.now()),
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

def ask(str):
    if "value of" in str:
        return ""
    try:
        data = wikipedia.summary(wikipedia.search(str)[0], sentences=2)
    except wikipedia.exceptions.DisambiguationError:
        data = ""
    except IndexError:
        data = ""
    return data
    
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
    
    info.update(dynamics)
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




#####Question  
    if text.startswith("what "):
        x = q_split(text)
        if q_type(text) == "def1":
            y = q_t1_proc(x)
            if y in info:
                say(info[y])
            elif y in sims:            
                say(info[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know what "+y+" is.")
        if q_type(text) == "def2":
            y = q_t1_proc(x)
            if y in info_was:
                say(info_was[y])
            elif y in sims:            
                say(info_was[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know what "+y+" was.")
        if q_type(text) == "time1":
            y = q_t1_proc(x)
            if y in time:
                say(time[y])
            elif y in sims:            
                say(time[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know when "+y+" is.")
    elif text.startswith("who "):
        x = q_split(text)
        if q_type(text) == "def1":
            y = q_t1_proc(x)
            if y in info:
                say(info[y])
            elif y in sims:            
                say(info[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know who "+y+" is.")
        if q_type(text) == "def2":
            y = q_t1_proc(x)
            if y in info_was:
                say(info_was[y])
            elif y in sims:            
                say(info_was[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know who "+y+" was.")
    elif text.startswith("where "):
        if text.endswith(" on"):
            text[:len(text)-3]
        if text.endswith(" in"):
            text[:len(text)-3]
        if text.endswith(" at"):
            text[:len(text)-3]
        x = q_split(text)
        if q_type(text) == "loc1":
            y = q_t1_proc(x)
            if y in location:
                say(location[y])
            elif y in sims:            
                say(location[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know where "+y+" is.")
        if q_type(text) == "loc2":
            y = q_t1_proc(x)
            if y in location_was:
                say(location_was[y])
            elif y in sims:            
                say(location_was[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know where "+y+" was.")
    elif text.startswith("when "):
        if text.endswith(" on"):
            text[:len(text)-3]
        if text.endswith(" in"):
            text[:len(text)-3]
        if text.endswith(" at"):
            text[:len(text)-3]
        x = q_split(text)
        if q_type(text) == "time1":
            y = q_t1_proc(x)
            if y in time:
                say(time[y])
            elif y in sims:            
                say(time[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know when "+y+" is.")
    elif text.startswith("how "):
        x = q_split(text)
        if q_type(text) == "def1":
            y = q_t1_proc(x)
            if y in info:
                say(info[y])
            elif y in sims:            
                say(info[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know how "+y+" is.")
        if q_type(text) == "def2":
            y = q_t1_proc(x)
            if y in info_was:
                say(info_was[y])
            elif y in sims:            
                say(info_was[sims[y]])
            else:
                x = ask(nocap)
                if x != "":
                    print(" Wikipedia tells me that:\n\n"+str(x)+"\n")
                else:
                    say("Sorry but, you don't know how "+y+" was.")


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
            eval(commands[text[0:findnth(text," ",3)]][8:].replace("_input_",nocap[findnth(nocap," ",3)+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:findnth(text," ",2)]] + " " + nocap[findnth(nocap," ",2)+1:])
    elif text[0:findnth(text," ",2)] in commands:
        if commands[text[0:findnth(text," ",2)]].startswith(":Python:"):
            eval(commands[text[0:findnth(text," ",2)]][8:].replace("_input_",nocap[findnth(nocap," ",2)+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:findnth(text," ",2)]] + " " + nocap[findnth(nocap," ",2)+1:])
    elif text[0:findnth(text," ",1)] in commands:
        if commands[text[0:findnth(text," ",1)]].startswith(":Python:"):
            eval(commands[text[0:findnth(text," ",1)]][8:].replace("_input_",nocap[findnth(nocap," ",1)+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:findnth(text," ",1)]] + " " + nocap[findnth(nocap," ",1)+1:])
    elif text[0:text.find(" ")] in commands:
        if commands[text[0:text.find(" ")]].startswith(":Python:"):
            eval(commands[text[0:text.find(" ")]][8:].replace("_input_",nocap[nocap.find(" ")+1:].replace("\\","\\\\").replace('"','\\\"').replace("'",'\\\'')))
        else:
            os.system(commands[text[0:text.find(" ")]] + " " + nocap[nocap.find(" ")+1:])
    elif text in commands:
        if commands[text].startswith(":Python:"):
            eval(commands[text][8:].replace("_input_",""))
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
    elif text.startswith("create "):
        if text[7:].startswith("templates"):
            print("[BOB] [INFO] Creating templates is required to install adons.")
            print("[BOB] [CAUTION] Do not do this if you have previously installed any addons you wish to keep.")
            x = input("[BOB] [???] Do you wish to proceed? ('Yes' to autheticate) \n>>> ")
            if x == "Yes":
                print("[BOB] Creating templates...")
                f = open(str(Path.home())+"/"+".commands.bob","w")
                f.write("{\n'say': ':Python:print(\"_input_\")',\n'echo': ':Python:print(\"_input_\")'\n}")
                f.close()
                f = open(str(Path.home())+"/"+".dynamics.bob","w")
                f.write("{\n'time': str(datetime.now()), \n'day': calendar.day_name[date.today().weekday()], \n'year': str(datetime.now()), \n'date': str(datetime.now())\n}")
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
    elif text.find("is") != -1 or text.find("are") != -1 or text.find("am") != -1:
        x = text
        remember(x)
    elif text.find("were") != -1 or text.find("was"):
        x = text
        remember(x)
        
#####Else
    else:
        say("Mi no comprehendo.")

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

    

