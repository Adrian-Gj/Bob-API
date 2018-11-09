import shutil
import os

import send2trash

from .multimedia import *
from .__init__ import *
from .cl import *

def command_open(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
            printbob("Can't find the specified file/program.")
def command_run(text,nocap,command):
    os.system(nocap[len(command):])
def command_edit(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
def command_create(text,nocap,command):
    printbob("[BOB] [INFO] Creating templates is required to install adons.")
    printbob("[BOB] [CAUTION] Do not do this if you have previously installed any addons you wish to keep.")
    x = input("[BOB] [???] Do you wish to proceed? ('Yes' to autheticate) \n>>> ")
    if x == "Yes":
        printbob("[BOB] Creating templates...")
        f = open(str(Path.home())+"/"+".commands.bob","w")
        f.write(str(commands))
        f.close()
        f = open(str(Path.home())+"/"+".dynamics.bob","w")
        f.write(str(dynamics))
        f.close()
        #f = open(str(Path.home())+"/"+".dynamics_sims.bob","w")
        #f.write("{\n\n}")
        #f.close()
        printbob("\nI have completed the creation of your templates.\nYou may now install addons.")
def command_move(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
        printbob("I can't find one of the files.")
def command_read(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
        printbob("I don't know where \""+nocap+"\" is")    
def command_mkdir(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
def command_delete(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
def command_play(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
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
def command_google(text,nocap,command):
    text = text[len(command):]
    nocap = nocap[len(command):]
    google(nocap)
def command_cd(text,nocap,command):
    try:
        os.chdir(nocap[len(command):].replace("~",str(Path.home())))
    except FileNotFoundError:
        printbob(""+"Sorry but I don't undersand where "+nocap[len(command):]+" is. Maybe you misspelt something.")
