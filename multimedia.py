from libs.lxml import html
import libs.wikipedia
import urllib.request
import sys
import os
from pathlib import Path

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
def ask(str):

    try:
        data = wikipedia.summary(wikipedia.search(str)[0], sentences=3)
    except wikipedia.exceptions.DisambiguationError:
        data = ""
    except IndexError:
        data = ""

    if ("value of" in str) and has_no(data) != True:
        x = 2
        while (has_no(data) != True) and (x<8):
            x += 1
            try:
                data = wikipedia.summary(wikipedia.search(str)[0], sentences=x)
            except wikipedia.exceptions.DisambiguationError:
                data = ""
            except IndexError:
                data = ""
        if x>7:
            try:
                data = wikipedia.summary(wikipedia.search(str)[0], sentences=3)
            except wikipedia.exceptions.DisambiguationError:
                data = ""
            except IndexError:
                data = ""
    return data
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
def search(string):
    x = string.split(" ")
    open_file("https://www.google.com/search?q="+string.replace("%","%25").replace("+","%2B").replace(" ","+"))
def google_com(str ,inp):
    print(" I don't know anything about: "+inp)
    print(" Do you want me to open a webrowser and google it for you?")
    x = input("?> ")
    if 'yes' in x.lower():
        search(str)
    else:
        print(" Ok I won't")
def google(str):
    print(" Do you want me to open a webrowser and google: '" +str+ "' for you?")
    x = input("?> ")
    if 'yes' in x.lower():
        search(str)
    else:
        print(" Ok I won't")
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

