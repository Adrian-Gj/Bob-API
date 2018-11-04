import libs.wikipedia
def mine( stri):
    name = "x"
    text = stri
    text = text.lower()
    text = text.replace(".0", ":0")\
           .replace(".1", ":1")\
           .replace(".2", ":2")\
           .replace(".3", ":3")\
           .replace(".4", ":4")\
           .replace(".5", ":5")\
           .replace(".6", ":6")\
           .replace(".7", ":7")\
           .replace(".8", ":8")\
           .replace(".9", ":9")\
           .replace(". ", ".")\
           .replace(",", "")\
           .replace("  ", " ")\
           .replace(" is also ", " is ")\
           .replace(" were ", " was ")\
           .replace(" was also ", " was ")\
           .replace(" who is", "."+name+" is")\
           .replace(" who was", "."+name+" was")\
           .replace(" who were", "."+name+" were")\
           .replace(" he is", "."+name+" is")\
           .replace(" she is", "."+name+" is")\
           .replace(" it is", "."+name+" is")\
           .replace(".he is", "."+name+" is")\
           .replace(".she is", "."+name+" is")\
           .replace(".it is", "."+name+" is")\
           .replace(" they is", "."+name+" is")\
           .replace(" are also ", " are ")\
           .replace(" who are", "."+name+" are")\
           .replace(" he are", "."+name+" are")\
           .replace(" she are", "."+name+" are")\
           .replace(" it are", "."+name+" are")\
           .replace(".he are", "."+name+" are")\
           .replace(".she are", "."+name+" are")\
           .replace(".it are", "."+name+" are")\
           .replace(" they are", "."+name+" are")\
           .replace("\n", ".")
    x = text.split(".")
    #print(text)
    out = []
    for item in x:
        sent = ""
        skip = False
        quote = False
        for let in item:
            if let == "(" and quote==False:
                skip = True
            if let == ";" and quote==False:
                skip = True
            if not skip:
                sent += let
            if let == ")" and quote==False:
                skip = False
            if let == "\"":
                skip = not skip
            sent = sent.replace(" are ", " is +> ").replace(" was ", " is *> ").replace(" were ", " is /> ").replace(" is ", ">1>2>",1)\
                   .replace("  "," ").replace(" >1>2>",">1>2>").replace("(","")\
                   .replace(")","").replace(" is +>", " are").replace(" is *>", " was")\
                   .replace(" is />", " were")
        #print(sent)
        if ">1>2>" in sent:
            out.append(sent)
    name2 = name.split(" ")[0]
    out = [out.replace(name2,name) for out in out]
    if len(name.split(" "))>1:
        name2 = name.split(" ")[1]
        out = [out.replace(name2,name) for out in out]
    if len(name.split(" "))>2:
        name2 = name.split(" ")[2]
        out = [out.replace(name2,name) for out in out]
    if len(name.split(" "))>3:
        name2 = name.split(" ")[3]
        out = [out.replace(name2,name) for out in out]
    out = [out.replace("he>1>2>",name+">1>2>") for out in out]
    out = [out.replace("she>1>2>",name+">1>2>") for out in out]
    out = [out.replace("it>1>2>",name+">1>2>") for out in out]
    out = [out.replace("they>1>2>",name+">1>2>") for out in out]
    out = [name+">1>2>"+out.split(">1>2>")[1] for out in out]
    out = [out.replace(" +> "," ") for out in out]
    out = [out.replace(" *> "," ") for out in out]
    out = [out.replace(" /> "," ") for out in out]
    #print(name)
    #print(name2)
    #print("")
    #print('\n'.join(map(str, out)))
    #print("")
    a = ""
    count = 1
    while count<len(out[0].split(">1>2>")):
        a += out[0].split(">1>2>")[count]
        #print()
        count += 1
    b = ""
    count = 1
    while count<len(out[1].split(">1>2>")):
        b += out[1].split(">1>2>")[count]
        #print()
        count += 1
    #print(a + " and is also "+b)
    x =    (a.replace(" +> "," ").replace("+> "," ")\
           .replace(" *> "," ").replace("*> "," ")\
           .replace(" /> "," ").replace("/> "," ")\
           + " and is also " + \
           b.replace(" +> "," ").replace("+> "," ")\
           .replace(" *> "," ").replace("*> "," ")\
           .replace(" /> "," ").replace("/> "," ")\
            ).replace("  "," ")
    while x.startswith(" "):
        x = x[1:]
    return x


#data = ""
#try:
#    data = libs.wikipedia.summary("Linus Torvalds",sentences=10)
#except libs.wikipedia.exceptions.DisambiguationError:
#    data = ""
#except IndexError:
#    data = ""
#print("Linus Torvalds is "+mine(data))
#print(data)
